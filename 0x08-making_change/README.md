# Change Making Project

This project focuses on implementing a solution to find the fewest number of coins needed to meet a given amount total. It includes an implementation of the `makeChange` function, which takes a pile of coins of different values and determines the optimal way to make change for a specified total.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [File Structure](#file-structure)
- [License](#license)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- PEP 8 style (version 1.7.x)
- All files must end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executable
- README.md file at the root of the project folder is mandatory

## Usage

The main functionality is provided in the `0-making_change.py` file. You can import the `makeChange` function and use it in your Python scripts.

```python
from 0-making_change import makeChange

# Example usage
result = makeChange([1, 2, 25], 37)
print(result)  # Output: 7
```

## Example

Here's a brief example of using the `makeChange` function:

```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```

## File Structure

- `0-making_change.py`: Contains the implementation of the `makeChange` function.
- `0-main.py`: Main file for testing the functionality.
