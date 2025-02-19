from importlib.metadata import version as _version
from .models import WaterQualityParameters
from .utils import check_water_quality

__version__ = _version("wqautils")
__all__ = ["WaterQualityParameters", "check_water_quality"]
