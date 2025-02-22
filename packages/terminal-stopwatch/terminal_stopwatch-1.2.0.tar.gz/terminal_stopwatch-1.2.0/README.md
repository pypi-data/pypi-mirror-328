# Terminal Stopwatch

A terminal-based stopwatch application featuring ASCII art time display and lap time functionality.


[![PyPI version](https://badge.fury.io/py/terminal-stopwatch.svg)](https://badge.fury.io/py/terminal-stopwatch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img src="stopwatch_final3.gif" width="302" alt="Terminal Stopwatch Demo">

## Features

- Large number display using ASCII art
- Lap time recording
- Simple keyboard shortcuts
- HH:MM:SS format for times over an hour
- MM:SS format for times under an hour
- Clean and intuitive terminal interface

## Installation

Using Poetry:
```bash
poetry add terminal-stopwatch
```

Using Pip:
```bash
pip install terminal-stopwatch
```

## Usage

### As a Package
```python
from terminal_stopwatch.main import main

main()
```

### From Command Line
```bash
# With Poetry
poetry run python -m terminal_stopwatch

# With Python
python -m terminal_stopwatch
```

## Controls

- `s` - Start/Pause
- `l` - Record Lap Time
- `r` - Reset
- `q` - Quit
- `Ctrl+C` - Force Quit

## Project Structure

```
terminal_stopwatch/
├── __init__.py        # Package initialization
├── constants.py       # Constants definition
├── models.py          # Data models (TimeDisplay)
├── terminal.py        # Terminal control
├── input_handler.py   # Input handling
├── stopwatch.py       # Stopwatch logic
└── main.py           # Main execution
```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/taejun0622/stopwatch.git
cd stopwatch
```

2. Set up Poetry environment:
```bash
poetry install
```

3. Run in development mode:
```bash
poetry run python run.py
```

## Dependencies

- Python 3.11+
- colorama - Terminal color support
- pyfiglet - ASCII art generation

## License

MIT License

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

- taejun (dugudugu0622@gmail.com)
- GitHub: [@taejun](https://github.com/taejun)

## Changelog

### [1.0.0] - 2024-02-20
- Initial Release
- Basic stopwatch functionality with ASCII art display
- Lap time recording feature
- Published to PyPI
