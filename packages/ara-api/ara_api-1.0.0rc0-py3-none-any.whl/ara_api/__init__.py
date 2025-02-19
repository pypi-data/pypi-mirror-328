from __future__ import annotations
from importlib.metadata import version

__version__ = version(__name__)

from .ara_lib import *


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
