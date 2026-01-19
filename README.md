# Guessing Game

A classic number guessing game implemented in Python!

## How It Works

The program generates a random number between 1 and 100, then challenges you to guess it. 
After each guess, you'll receive feedback telling you whether your guess is too high, too low, or correct. 
The game continues until you guess the correct number.

## Features

- Random number generation between 1-100
- Input validation (non-numeric input is ignored)
- Clear feedback for each guess
- Congratulatory message when you win


## Installation

1. Install uv if you haven't already:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

2. Clone the repository:

```bash
git clone dbozbay/python-guessing-game.git
cd python-guessing-game
```

3. Install dependencies:

```bash
uv sync
```

## Usage

Run the game from the command line:

```bash
uv run main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


