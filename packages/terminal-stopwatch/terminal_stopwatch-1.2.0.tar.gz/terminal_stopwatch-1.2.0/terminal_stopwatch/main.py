"""스톱워치 메인 실행 파일"""

from colorama import init

from terminal_stopwatch.stopwatch import Stopwatch
from terminal_stopwatch.terminal import TerminalController
from terminal_stopwatch.input_handler import InputHandler
from terminal_stopwatch.constants import CONTROLS

def main():
    stopwatch = Stopwatch()
    terminal = TerminalController()
    input_handler = InputHandler()
    
    terminal.clear_screen()
    terminal.hide_cursor()
    
    try:
        while True:
            terminal.clear_screen()
            elapsed = stopwatch.get_elapsed()
            
            terminal.display_time(elapsed)
            terminal.display_laps(stopwatch.laps)
            
            print("\nControls:")
            for key, description in CONTROLS.items():
                print(f"[{key}] - {description}")
            print("\nEnter command: ", end='', flush=True)

            user_input = input_handler.get_input_with_timeout()
            if user_input in CONTROLS:
                if user_input == 's':
                    if stopwatch.running:
                        stopwatch.pause()
                    else:
                        stopwatch.start()
                elif user_input == 'l':
                    stopwatch.lap()
                elif user_input == 'r':
                    stopwatch.reset()
                elif user_input == 'q':
                    terminal.clear_screen()
                    terminal.show_cursor()
                    print("Stopwatch stopped.")
                    break

    except KeyboardInterrupt:
        terminal.clear_screen()
        terminal.show_cursor()
        print("\nInterrupted. Stopwatch stopped.")

if __name__ == "__main__":
    init()  # colorama 초기화
    main()

