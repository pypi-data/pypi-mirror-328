from importlib.metadata import version as metadata_version, PackageNotFoundError

try:
    __version__ = version = metadata_version("nirtorch")
    del metadata_version
except PackageNotFoundError:
    # package is not installed
    pass