from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("requea_decoder")
except PackageNotFoundError:
    # package is not installed
    pass