import os
from importlib.metadata import version, PackageNotFoundError

def get_version():
    try:
        # Attempt to get the version from the installed package
        return version("bdx")  # Change to the name specified in setup.cfg
    except PackageNotFoundError:
        # Fallback to reading from setup.cfg if not installed
        return read_version_from_setup_cfg()

def read_version_from_setup_cfg():
    setup_cfg_path = os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')  # Adjust the path as needed
    if os.path.exists(setup_cfg_path):
        with open(setup_cfg_path) as f:
            for line in f:
                if line.startswith("version ="):
                    return line.split("=", 1)[1].strip()
    return "unknown"  # Default value if version can't be found

__version__ = get_version()
