"""터미널 제어 관련 기능"""

import os
from typing import List
import pyfiglet
from colorama import Cursor, Style

from terminal_stopwatch.models import TimeDisplay

class TerminalController:
    @staticmethod
    def clear_screen():
        os.system('clear')

    @staticmethod
    def move_cursor_up(lines: int):
        print(Cursor.UP(lines), end='')

    @staticmethod
    def clear_from_cursor():
        print('\033[J', end='')

    @staticmethod
    def clear_line():
        print("\033[K", end="")

    @staticmethod
    def hide_cursor():
        print("\033[?25l", end='')

    @staticmethod
    def show_cursor():
        print("\033[?25h", end='')

    @staticmethod
    def display_time(elapsed: float):
        time_display = TimeDisplay.from_seconds(elapsed)
        ascii_art = pyfiglet.figlet_format(str(time_display))
        for line in ascii_art.split('\n'):
            if line.strip():
                print(f"{Style.BRIGHT}{line}{Style.RESET_ALL}")

    @staticmethod
    def display_laps(laps: List[float]):
        if not laps:
            return
        
        print("Lap Times:")
        for idx, lap in enumerate(laps, 1):
            time_display = TimeDisplay.from_seconds(lap)
            print(f"Lap {idx}: {Style.BRIGHT}{time_display}{Style.RESET_ALL}")
        print("-" * 40) 