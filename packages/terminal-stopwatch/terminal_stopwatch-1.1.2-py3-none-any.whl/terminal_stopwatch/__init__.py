"""
Terminal Stopwatch - A terminal-based stopwatch application featuring ASCII art display
"""

from .stopwatch import Stopwatch
from .terminal import TerminalController
from .input_handler import InputHandler
from .models import TimeDisplay
from .constants import CONTROLS, REFRESH_RATE

__all__ = [
    'Stopwatch',
    'TerminalController',
    'InputHandler',
    'TimeDisplay',
    'CONTROLS',
    'REFRESH_RATE',
]

__version__ = "1.1.2" 