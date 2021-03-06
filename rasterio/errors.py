"""Errors and Warnings."""

from click import FileError


class RasterioError(Exception):
    """Root exception class"""


class WindowError(RasterioError):
    """Raised when errors occur during window operations"""


class CRSError(ValueError):
    """Raised when a CRS string or mapping is invalid or cannot serve
    to define a coordinate transformation."""


class EnvError(RasterioError):
    """Raised when the state of GDAL/AWS environment cannot be created
    or modified."""


class DriverRegistrationError(ValueError):
    """Raised when a format driver is requested but is not registered."""


class FileOverwriteError(FileError):
    """Raised when Rasterio's CLI refuses to clobber output files."""

    def __init__(self, message):
        """Raise FileOverwriteError with message as hint."""
        super(FileOverwriteError, self).__init__('', hint=message)


class RasterioIOError(IOError):
    """Raised when a dataset cannot be opened using one of the
    registered format drivers."""


class NodataShadowWarning(UserWarning):
    """Warn that a dataset's nodata attribute is shadowing its alpha band."""

    def __str__(self):
        return ("The dataset's nodata attribute is shadowing "
                "the alpha band. All masks will be determined "
                "by the nodata attribute")


class NotGeoreferencedWarning(UserWarning):
    """Warn that a dataset isn't georeferenced."""


class GDALBehaviorChangeException(RuntimeError):
    """Raised when GDAL's behavior differs from the given arguments.  For
    example, antimeridian cutting is always on as of GDAL 2.2.0.  Users
    expecting it to be off will be presented with a MultiPolygon when the
    rest of their code expects a Polygon.

        # Raises an exception on GDAL >= 2.2.0
        rasterio.warp.transform_geometry(
            src_crs, dst_crs, antimeridian_cutting=False)
    """

class WindowEvaluationError(ValueError):
    """Raised when window evaluation fails"""


class RasterioDeprecationWarning(UserWarning):
    """Rasterio module deprecations"""


class RasterBlockError(RasterioError):
    """Raised when raster block access fails"""
