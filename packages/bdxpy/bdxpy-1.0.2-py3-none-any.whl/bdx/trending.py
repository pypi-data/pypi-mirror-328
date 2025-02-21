from __future__ import annotations
from enum import Enum
from pandas import DataFrame
from requests import Response

from .common import _handle_http_error

from .types import AggregationLevel, TimeFrame, TimeframeType
from dataclasses import dataclass
from datetime import datetime
from hashlib import sha1
import dacite

_TREND_VALUE_PROPERTIES = {  
                "label",
                "color",
                "axis",
                "lineStyle",
                "dataTableOnly",
                "glyphStyle",
                "visualization",
                "shownByDefault",
                "manualBucketSizing",
                "bucketCount",
                "bucketSize",
                "bucketStart",
                "bucketAggregation"                
            }

def _add_trend_value_properties_to_selector(sel : dict, pd : dict) -> None:
    for k in pd:
        if k in _TREND_VALUE_PROPERTIES:
            val = pd[k]
            if isinstance(val, Enum):
                val = val.value
            elif isinstance(val, bool):
                val = "true" if val else "false"

            sel[k] = val

def _sha1_to_hex(input):
    sha1_hash = sha1()
    sha1_hash.update(input.encode('utf-8'))
    hex_digest = sha1_hash.hexdigest()
    return hex_digest

class PropertyDescriptor:
    """
    Contains the bare minimum of information required to retrieve a set
    of data values from the BDX trending service.
    """
    componentPathId : int
    propertyName : str

    #
    # If componentPathId is None, contains the key-based virtual path
    # of the target component. The path can be interpreted by the virtual
    # tree service and resolved to a data object.
    #
    virtualPath : str        

    def __init__(self, componentPathId : int, propertyName : str, virtualPath : str = None) -> None:
        """
        Initializes a property descriptor

        Parameters
        ----------
        componentPathId : int
            Component path ID for which to retrieve data
        propertyName : str
            The name of a component property to retrieve
        virtualPath : str, optional
            If the specified component is virtual, componentPath may be specified as None
            and this parameter set to a non-null value to supply the retrieval path. The default value is None
        """
        self.componentPathId = componentPathId
        self.propertyName = propertyName
        self.virtualPath = virtualPath

class CartesianRetrievalResult:
    """
    Contains the result of data retrieval in a cartesian (two-dimensional) dataset.

    The actual values are returned in the DataFrame accessible via the dataframe property.

    For each column in the DataFrame there will be a corresponding column descriptor (matched by name)
    in the dictionary returned by the columnInformation property. The descriptor contains additional
    information about the data in the associated column, such as TrendView properties like color,
    glyph style and full column label.
    """
    _data_frame : DataFrame
    _column_info : dict

    def _dict_to_value(self, d : dict) -> tuple:
        value_type = d["valueType"]
        value = None

        if value_type == "REAL":
            value = d["realValue"] if "realValue" in d else None
        elif value_type == "INTEGER":
            value = d["intValue"] if "intValue" in d else None
        elif value_type == "STRING":
            value = d["stringValue"] if "stringValue" in d else None
        elif value_type == "BOOL":
            value = d["boolValue"] if "boolValue" in d else None
            if value is not None:
                value = False if str(value).upper() == "FALSE" else True

        #
        # Time will have the local timezone
        #         
        time = datetime.fromisoformat(d["time"]).astimezone(tz = None)

        return (time, value)


    def _create_column(self, trend_value : dict) -> tuple:

        col_name = trend_value["componentPathId"] if "componentPathId" in trend_value else _sha1_to_hex(trend_value["virtualPath"])
        col_name = f"{col_name}_{trend_value['propertyName']}"

        dv_list = []

        if "dataValues" in trend_value:
            for val in trend_value["dataValues"]:
                dv_list.append(self._dict_to_value(val))

        col_info = {
            "propertyName": trend_value["propertyName"] if "propertyName" in trend_value else None,
            "componentPathId": trend_value["componentPathId"] if "componentPathId" in trend_value else None,
            "virtualPath": trend_value["virtualPath"] if "virtualPath" in trend_value else None
        }

        additional_properties = { k:v for k, v in trend_value.items() if k in _TREND_VALUE_PROPERTIES }

        col_info = col_info | additional_properties

        if "deviceInfo" in trend_value:
            col_info["deviceInfo"] = trend_value["deviceInfo"]

        return (col_name, DataFrame(dv_list, columns=["time", col_name]), col_info)

    def __init__(self, json : list) -> None:
        df = DataFrame([], columns=["time"])
        ci = { }

        for col in json:
            if len(col["trendValues"]) > 0:
                (col_name, col_df, col_info) = self._create_column(col["trendValues"][0])
                ci[col_name] = col_info
                df = df.merge(col_df, "outer", on="time")

        self._data_frame = df
        self._column_info = ci

    @property
    def dataframe(self) -> DataFrame:
        """
        Retrieves the DataFrame filled with retrieval results

        Returns
        -------
        DataFrame
            Retrieved data
        """
        return self._data_frame
    
    @property
    def column_information(self) -> dict:
        """
        Retrieves the column information detail associated with retrieved data

        Returns
        -------
        dict
            A dictionary of column data, by column name, with additional column properties
        """
        return self._column_info
    
class TrendType(Enum):
    """
    Types of trends in TrendView
    """
    LINE_CHART = "LineChart"
    COLUMN_CHART = "ColumnChart"
    SCATTER_PLOT = "ScatterPlot"
    SINGLE_VARIABLE_HEAT_MAP = "SingleVariableHeatMap"
    MULTI_VARIABLE_HEAT_MAP = "MultiVariableHeatMap"

class HeatMapVisualization(Enum):
    HEAT_MAP = "HeatMap"
    SURFACE = "Surface"

class HeatMapCompVisualization(Enum):
    LINE = "Line"
    BAR = "Bar"

class TimeAxisCategorization(Enum):

    #
    # Day categorizations
    #
    
    DAY_OF_MONTH = "DayOfMonth"
    DAY_OF_WEEK = "DayOfWeek"
    
    #
    # Week categorizations
    #
    
    WEEK_OF_MONTH = "WeekOfMonth"
    WEEK_OF_YEAR = "WeekOfYear"


@dataclass
class TrendSummary:
    """
    Contains summary information about a TrendView trend
    """
    _parent : Trending | None

    #
    # Trend ID
    #
    trendId : int

    #
    # Trend name (label)
    #
    name : str

    #
    # Trend trendType
    #
    trendType : TrendType

    #
    # List of keywords, associated with the trend
    #
    keywords : list[str]

    #
    # Set of linked building IDs
    #
    buildingIds : list[int]
    
    #
    # Indicates whether the current user can update the trend
    #
    updatable : bool
    
    defPrimaryVisualization : HeatMapVisualization = None
    
    defColorScheme : str = None
    
    invertColorScheme : bool = False
    
    showColorBar : bool = False
    
    colorBarLabel : bool = False
    
    defDataTimeframe : TimeframeType = None
    
    defDataAggregation : AggregationLevel = None
    
    windowSize : AggregationLevel = None
    
    timeframeAxis : AxisSelection = None
    
    showCompSeries : bool = False
    
    defCompVisualization : HeatMapCompVisualization = None
    
    positiveValueColor : int = None
    
    negativeValueColor : int = None
    
    timeAxisAggregation : AggregationLevel = None
    
    timeAxisCategorization : TimeAxisCategorization = None

    timeAxisLabel : str = None

class AxisSelection(Enum):
    """
    Axis selection for a TrendView trend value (series)
    """
    Y1 = "Y1"
    Y2 = "Y2"
    X = "X"
    Z = "Z"

class LineStyle(Enum):
    """
    TrendView trend value (series) line style
    """
    NORMAL = "normal"
    DASHED = "dashed"
    BOLD = "bold"

class GlyphStyle(Enum):
    """
    TrendView trend value (series) glyph style
    """
    SQUARE = "Square"
    CIRCLE = "Circle"
    DIAMOND = "Diamond"
    TRIANGLE_UP = "TriangleUp"
    TRIANGLE_DOWN = "TriangleDown"
    TRIANGLE_LEFT = "TriangleLeft"
    TRIANGLE_RIGHT = "TriangleRight"

class HeatMapSeriesVisualization(Enum):
    PRIMARY = "Primary"
    COMPARISON = "Comparison"

class BucketAggregation(Enum):

    #
    # Numeric aggregations
    #
    
    AVERAGE = "Average"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    COUNT = "Count"
    SUM = "Sum"
    
    #
    # Boolean aggregations
    #
    
    PERCENT_TRUE = "PercentTrue"
    PERCENT_FALSE = "PercentFalse"
    ANY_TRUE = "AnyTrue"            # 1 if any value is true, 0 otherwise
    ANY_FALSE = "AnyFalse"          # 1 if all values are true, 0 otherwise
    COUNT_TRUE = "CountTrue"
    COUNT_FALSE = "CountFalse"

@dataclass
class TrendValue:
    """
    Contins information associated with a TrendView trend value (series)
    """
    trendValueId : int

    componentPathId : int | None
    propertyName : str

    #
    # If componentPathId is None, contains the key-based virtual path
    # of the target component. The path can be interpreted by the virtual
    # tree service and resolved to a data object.
    #
    virtualPath : str | None
    
    #
    # Display label
    #
    label : str

    #
    # Display color for the chart
    #
    color : int

    #
    # Axis selection (Y1 or Y2)
    #
    axis : AxisSelection

    #
    # If true, the values are only displayed in the data table, not the chart
    #
    dataTableOnly : bool | None
    
    #
    # Heat map visualization, primary or comparison series
    #
    visualization : HeatMapSeriesVisualization | None
    
    #
    # true if this is the default series for the specified visualization
    #
    shownByDefault : bool |None
    
    #
    # true if buckets are sized manually for a multi-value heat map axis
    #
    manualBucketSizing : bool | None

    #
    # Bucket count for auto-sized heat map axes
    #
    bucketCount : int | None
    
    #
    # Bucket size for manually sized heat map buckets
    #
    bucketSize : float | None
    
    #
    # First bucket start value for manually sized heat map buckets
    #
    bucketStart : float | None
    
    #
    # For heat map value axes - bucket aggregation to use
    #
    bucketAggregation : BucketAggregation | None

    #
    # if true, indicates that this property must always be resolved from a 
    # virtual path in order to get the proper value.  There is no other way to 
    # access the data that they desire at this path.  If false, if the 
    # caller chooses they can determine a different method to record where 
    # the data comes from and it should still be accessible.
    #
    forceVirtualPath : bool = False

    #
    # indicates the style of line that should be rendered for this series 
    # Current options are normal, dashed, and bold. 
    #    
    lineStyle : LineStyle = LineStyle.NORMAL

    #
    # Series glyph style
    #
    glyphStyle : GlyphStyle = GlyphStyle.CIRCLE

@dataclass
class Trend(TrendSummary):
    """
    Contains information about a TrendView trend, along with all associated trend series
    """
    values : list[TrendValue] | None = None

    def __post_init__(self):
        if self.values is None:
            self.values = []

    def retrieve_data(self, timeframe : TimeFrame = TimeFrame.last_7_days(), aggregation_level : AggregationLevel | None = None) -> CartesianRetrievalResult :
        """
        Retrives data from this TrendView trend

        Parameters
        ----------
        timeframe : TimeFrame, optional
            Timeframe for which to retrieve the data. Defaults to TimeFrame.last7Days()
        aggregation_level : AggregationLevel | None, optional
            Aggregation level at which to retrieve data, by default None (point-level).

        Returns
        -------
        CartesianRetrievalResult
            Retrieved data and associated column detail

        Raises
        ------
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        return self._parent.retrieve_data(self.values, timeframe=timeframe, aggregation_level=aggregation_level)    

def _trend_mapping_config() -> dacite.Config:
    return dacite.Config(type_hooks = {
        AxisSelection: lambda v: AxisSelection(v),
        HeatMapSeriesVisualization: lambda v: HeatMapSeriesVisualization(v),
        BucketAggregation: lambda v: BucketAggregation(v),
        LineStyle: lambda v: LineStyle(v),
        GlyphStyle: lambda v: GlyphStyle(v),
        HeatMapVisualization: lambda v: HeatMapVisualization(v),
        TimeframeType: lambda v: TimeframeType(v),
        AggregationLevel: lambda v: AggregationLevel(v),
        AxisSelection: lambda v: AxisSelection(v),
        HeatMapCompVisualization: lambda v: HeatMapCompVisualization(v),
        TimeAxisCategorization: lambda v: TimeAxisCategorization(v),
        TrendType: lambda v: TrendType(v)
    })
    
class Trending:
    _parent = None
    _api_root : str

    def __init__(self, parent) -> None:
        self._parent = parent
        self._api_root = f"{self._parent.host_url}/trendview/api"

    def retrieve_data(self,
                 properties : list,
                 timeframe : TimeFrame = TimeFrame.last_7_days(),
                 aggregation_level : AggregationLevel = None) -> CartesianRetrievalResult:
        """
        Retrieves data from TrendView

        Parameters
        ----------
        properties : list
            A list of PropertyDescriptor-like objects describing what information to retrieve.
            These can be actual PropertyDescriptors, or dictionaries with matching attribute names.
            At least componentPathId and propertyName or virtualPath and propertyName must be provided.
        timeframe : TimeFrame, optional
            An optional timeframe for data retrieva. Defaults to TimeFrame.last7Days()
        aggregation_level : AggregationLevel, optional
            An optional aggregation level for data to retrieve. Defaults to None, which means point-level data

        Returns
        -------
        CartesianRetrievalResult
            Retrieved data and associated column detail

        Raises
        ------
        HttpRequestError
            There was an error in HTTP communications with the server
        """

        clean_selector_list = []

        for prop in properties:
            pd = prop if isinstance(prop, dict) else prop.__dict__

            sel = { }

            if pd.get("componentPathId") is not None and pd.get("propertyName") is not None:
                if bool(pd.get("forceVirtualPath")) and pd.get("virtualPath") is not None:
                    sel["virtualPath"]  = pd["virtualPath"]
                    sel["propertyName"] = pd["propertyName"]
                else:
                    sel["componentPathId"] = pd["componentPathId"]
                    sel["propertyName"] = pd["propertyName"]
            elif pd.get("virtualPath") is not None and pd.get("propertyName") is not None:
                sel["virtualPath"]  = pd["virtualPath"]
                sel["propertyName"] = pd["propertyName"]
            else:
                continue

            _add_trend_value_properties_to_selector(sel, pd)
            clean_selector_list.append(sel)

        params = {
            "startDate": timeframe.start_to_ISO_string(),
            "endDate": timeframe.end_to_ISO_string(),
            "aggregationLevel": AggregationLevel.to_disp_aggregation_level(aggregation_level),
            "selectorList": clean_selector_list
        }

        resp : Response = self._parent.session.post(f"{self._api_root}/data-values/grouped", json=params)

        if not resp.ok:
            _handle_http_error(resp)

        return CartesianRetrievalResult(resp.json())
    
    def trends(self, trend_id : int | None = None) -> Trend | list[TrendSummary]:
        """
        Returns a TrendView trend by its specified ID, or a list of all accessible trends.

        Parameters
        ----------
        trend_id : int | None, optional
            An optional trend ID to retrieve. This parameter is optional. If it is specified,
            a single trend is retrieved. If it is omitted, a summary list of all trends
            accessible to the current user is returned.

        Returns
        -------
        Trend | list[TrendSummary]
            Specified trend if trend ID is supplied, otherwise a list of all accessible
            trend summaries.

        Raises
        ------
        DataNotFoundError
            A trend ID was supplied and specified trend cannot be found
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        resp : Response

        if trend_id is None:
            resp = self._parent.session.get(f"{self._api_root}/trend-summaries")

            if not resp.ok:
                _handle_http_error(resp)
            
            json = resp.json()
            return [ dacite.from_dict(data_class = TrendSummary, data = rec, config = _trend_mapping_config()) for rec in json ]

        else:
            resp = self._parent.session.get(f"{self._api_root}/trend-info/{trend_id}")

            if not resp.ok:
                _handle_http_error(resp)
            
            json = resp.json()
            trend = dacite.from_dict(data_class = Trend, data = json, config = _trend_mapping_config())
            trend._parent = self
            return trend
