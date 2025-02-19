"""Code for Daft"""

from importlib.metadata import version as get_distribution

from . import _core, _exceptions, _utils
from ._core import PGM, Node, Edge, Plate, Text
from ._exceptions import SameLocationError
from ._utils import _rendering_context, _pop_multiple

__version__ = get_distribution("daft")
__all__ = []
__all__ += _core.__all__
__all__ += _exceptions.__all__
__all__ += _utils.__all__
import warnings

warnings.warn(
    "The 'daft' package has been renamed to 'daft-pgm' and will be yanked from PYPI on 2025/03/03.\n"
    "Please uninstall 'daft' and install 'daft-pgm' instead using:\n"
    "    pip uninstall daft\n"
    "    pip install 'daft-pgm'",
    DeprecationWarning,
    stacklevel=2
)
