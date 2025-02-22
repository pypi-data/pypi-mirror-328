import sys

version_info = (0, 1, 1)
__version__ = '0.1.1'

__all__ = ["win32", "gnu", "darwin"]

from .darwin import *
from .win32 import *
from .gnu import *
