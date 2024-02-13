# Prime Game

## Description
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

This project provides a Python implementation to determine the winner of each game session based on a given number of rounds and the upper limits for each round.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)
- Allowed editors: vi, vim, emacs

## Usage
To determine the winner of the Prime Game, run the provided `main.py` script with the desired number of rounds and upper limits for each round.

Example:
```bash
./main.py
```

## Files
- `0-prime_game.py`: Python module containing the implementation of the Prime Game.
- `main.py`: Script to test the Prime Game implementation.

## Functionality
The `isWinner` function in `0-prime_game.py` takes two arguments:
1. `x`: Number of rounds.
2. `nums`: List of integers representing the upper limits for each round.

It returns the name of the player who won the most rounds, or `None` if the winner cannot be determined.

## Example
```python
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
```
