from .core import *
from .stubs import *
from .scripts.editor import editor
from .scripts.deploy import deploy

core.__all__.append('editor')
__all__ = core.__all__

version = '0.2.5 Released 18-FEBRUARY-2025'

__version__ = ver = version.split()[0]