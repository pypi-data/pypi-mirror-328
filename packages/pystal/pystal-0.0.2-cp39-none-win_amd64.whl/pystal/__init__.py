import sys
import platform
from pathlib import Path


if platform.system() == "Windows":
    try:
        from .win.pycrystal_core import *
    except ImportError as e:
        raise RuntimeError("Windows components are missing, please reinstall") from e
elif platform.system() == "Linux":
    from .linux.pycrystal_core import *
else:
    raise NotImplementedError("Only supports Windows and Linux platforms")
    



    