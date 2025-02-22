import sys

version_info = (0, 1, 2)
__version__ = '0.1.2'

__all__ = ["win32", "gnu", "darwin"]

from .darwin import *
from .win32 import *
from .gnu import *
