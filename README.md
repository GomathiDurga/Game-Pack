# 🎮 Game Pack CLI

**3 classic games in one terminal app**: Number Guessing, Hangman, Rock Paper Scissors with score tracking.

## Features
- 🔢 Number Guessing (1-100, 7 attempts)
- 🧍 Hangman (6 wrong guesses)
- ✂️ Rock Paper Scissors (best of 3)
- 🏆 Score system across games


## Commands
| Command | Description | Points |
|---------|-------------|--------|
| `1` | Number Guessing (1-100) | 10-70 |
| `2` | Hangman (guess word) | 50 |
| `3` | Rock Paper Scissors | 30 |
| `4` | Quit & show final score | - |

## Games Details
| Game | Rules | Win Condition |
|------|-------|---------------|
| **Number Guessing** | Guess 1-100 in ≤7 tries | Exact match |
| **Hangman** | Guess letters, 6 wrong max | Solve word |
| **RPS** | Rock/Paper/Scissors | Win 2/3 rounds |

## Tech Stack
- Python 3.x
- `random` module
- OOP (class-based)
- Cross-platform (Windows/Mac/Linux)

## Setup & Run
```bash
python game_pack.py
