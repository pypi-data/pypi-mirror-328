from __future__ import annotations
import datetime
from enum import Enum
from dataclasses import dataclass

class TimeFrame:
    """
    Represents a timeframe in BDX
    """
    start_time : datetime.datetime = None
    end_time : datetime.datetime = None

    def __init__(self, start=None, end=None) -> None:
        """
        Constructs a timeframe with the specified start and end times

        Parameters
        ----------
        start : datetime, optional
            Start time, by default None
        end : datetime, optional
            End time, by default None
        """
        super().__init__()
        self.start_time = start
        self.end_time = end

    @staticmethod
    def last_n_days(n : int = 7) -> TimeFrame:
        """
        Creates a trailing timeframe of the specified number
        of days before the current time. The start time is rounded down to
        the start of the day.

        Parameters
        ----------
        n : int, optional
            Number of days, by default 7

        Returns
        -------
        TimeFrame
            Timeframe of the specified number of days before current time
        """
        now = datetime.datetime.now()
        days_ago = (now - datetime.timedelta(days=n)).replace(hour=0, minute=0, second=0, microsecond=0)
        return TimeFrame(days_ago, now)

    @staticmethod
    def last_n_weeks(n : int = 1) -> TimeFrame:
        """
        Creates a trailing timeframe of the specified number
        of weeks before the current time. The start time is rounded down to
        the start of the day.

        Parameters
        ----------
        n : int, optional
            Number of weeks, by default 1

        Returns
        -------
        TimeFrame
            Timeframe of the specified number of weeks before current time
        """
        now = datetime.datetime.now()
        days_ago = (now - datetime.timedelta(weeks=n)).replace(hour=0, minute=0, second=0, microsecond=0)
        return TimeFrame(days_ago, now)

    @staticmethod
    def last_7_days() -> TimeFrame:
        """
        Returns a timeframe, which begins on the day start 7 days prior to today
        and ends at current time.

        Returns
        -------
        TimeFrame
            Trailing 7-day timeframe
        """
        return TimeFrame.last_n_days(7)
    
    @staticmethod
    def last_30_days() -> TimeFrame:
        """
        Returns a timeframe, which begins on the day start 30 days prior to today
        and ends at current time.

        Returns
        -------
        TimeFrame
            Trailing 30-day timeframe
        """
        return TimeFrame.last_n_days(30)
    
    @staticmethod
    def datetime_to_ISO_string(dt : datetime.datetime | None) -> str:
        """
        Returns the specified datetime expressed as an ISO-8601 string.

        Parameters
        ----------
        dt : datetime.datetime | None
            Datetime to transform or None

        Returns
        -------
        str
            ISO-8601 representation of the specified datetime or None if the parameter is None
        """
        return dt if dt is None else dt.astimezone().replace(microsecond=0).isoformat()

    def start_to_ISO_string(self) -> str:
        """
        Returns this timeframe's start time in ISO-8601 format.

        Returns
        -------
        str
            Start time in ISO-8601 format or None if ther is no start time
        """
        return TimeFrame.datetime_to_ISO_string(self.start_time)
    
    def end_to_ISO_string(self) -> str:
        """
        Returns this timeframe's end time in ISO-8601 format.

        Returns
        -------
        str
            End time in ISO-8601 format or None if there is no end time
        """
        return TimeFrame.datetime_to_ISO_string(self.end_time)

class AggregationLevel(Enum):
    """
    A list of all possible aggregation levels in BDX.
    """
    POINT = "Point"
    HOURLY = "Hourly"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"

    @staticmethod
    def to_disp_aggregation_level(al) -> str:
        if al is None:
            return "Point"
        else:
            if isinstance(al, AggregationLevel):
                return al.value
            else:
                return None

class TimeframeType(Enum):
    """
    A list of standard timeframe types in BDX.
    """
    TODAY = "today"
    LAST_7_DAYS = "last7Days"
    MONTH_TO_DATE = "monthToDate"
    LAST_30_DAYS = "last30Days"
    YEAR_TO_DATE = "yearToDate"
    LAST_12_MONTHS = "last12Months"
    LAST_3_YEARS = "last3Years"

class AuthenticationError(Exception):
    """
    This exception is raised if there is an authentication problem with the BDX server.
    """
    def __init__(self, reason: str | None, http_code: str | None = None, login_result: str | None = None, cause: str | None = None, *args: object) -> None:
        super().__init__(reason, *args)
        self.reason = reason
        self.http_code = http_code
        self.login_result = login_result

class HttpRequestError(Exception):
    """
    This exception is raised if there is a problem in HTTP communications with the BDX server.
    """
    def __init__(self, http_status : int, http_message : str | None = None, *args: object) -> None:
        super().__init__(*args)
        self.http_status = http_status
        self.http_message = http_message

class DataNotFoundError(Exception):
    """
    This exception is raised when a record is not found during a data retrieval operation.
    """
    key = None

    def __init__(self, key, *args: object) -> None:
        super().__init__(*args)
        self.key = key

class SecurityError(Exception):
    """
    This exception is raised when the user attempts to access a BDX API method, which he/she
    is not allowed to use due to role-based security, or an access control list (ACL) violation
    is detected.
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ResourceType(Enum):
    """
    A list of all meter resource types in BDX.
    """
    CUSTOM = "Custom"
    ELECTRIC = "Electric"
    GAS = "Gas"
    CHILLED_WATER = "ChilledWater"
    HOT_WATER = "HotWater"
    STEAM_SUPPLY = "SteamSupply"
    STEAM_CONDENSATE = "SteamCondensate"
    FUEL = "Fuel"
    BTU = "Btu"

@dataclass
class Image:
    """
    Contains information about an image or an icon.
    """
    imageId : int
    name : str
    data : bytearray | None

