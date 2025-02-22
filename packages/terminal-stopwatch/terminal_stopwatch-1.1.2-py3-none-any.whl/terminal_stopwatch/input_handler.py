"""입력 처리 관련 기능"""

import sys
import select
import tty
import termios
from typing import Optional

from terminal_stopwatch.constants import REFRESH_RATE

class InputHandler:
    @staticmethod
    def get_input_with_timeout() -> Optional[str]:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            r, _, _ = select.select([sys.stdin], [], [], REFRESH_RATE)
            if r:
                return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None 