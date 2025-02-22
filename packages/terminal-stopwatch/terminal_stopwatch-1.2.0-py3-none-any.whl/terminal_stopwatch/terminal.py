"""터미널 제어 관련 기능"""

import os
from typing import List
from colorama import Cursor, Style

from terminal_stopwatch.models import TimeDisplay
from terminal_stopwatch.ascii_numbers import NUMBERS

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
        time_str = str(time_display)
        
        # 각 숫자의 높이만큼 반복
        for line_idx in range(5):
            line = ""
            # 시간 문자열의 각 문자에 대해
            for char in time_str:
                if char == ' ':
                    line += " "  # 시:분:초 구분자 사이 간격
                    continue
                # 숫자나 콜론의 해당 라인 가져오기
                char_line = NUMBERS[char][line_idx]
                line += char_line
            print(f"{Style.BRIGHT}{line}{Style.RESET_ALL}")
        print()  # 시간 표시 후 한 줄 띄우기

    @staticmethod
    def display_laps(laps: List[float]):
        if not laps:
            return
        
        print("Lap Times:")
        for idx, lap in enumerate(laps, 1):
            time_display = TimeDisplay.from_seconds(lap)
            print(f"Lap {idx}: {Style.BRIGHT}{time_display}{Style.RESET_ALL}")
        print("-" * 40) 