import os
from pathlib import Path

# Automatically set SERENITY_RESOURCES
package_dir = Path(__file__).resolve().parent.parent
resources_dir = package_dir / "share" / "serenity" / "data"
if resources_dir.exists():
    os.environ["SERENITY_RESOURCES"] = str(resources_dir) + "/"

laplace_dir = package_dir / "share" / "laplace-minimax"
if laplace_dir.exists():
    os.environ["LAPLACE_ROOT"] = str(laplace_dir)

from .fragment import fragment
from .CubeUtils import addCubes, subtractCubes
from .redirectOutput import redirectOutputToFile
from .spectrum import parseSpectrum

__all__ = ["fragment", "addCubes", "subtractCubes", "redirectOutputToFile", "parseSpectrum"]

# Conditionally import plotSpectrum if matplotlib is available
try:
    from .spectrum import plotSpectrum
    __all__.append("plotSpectrum")
except ImportError:
    pass