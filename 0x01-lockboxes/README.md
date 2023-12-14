# Lockboxes

## Description

A Python module for working with lockboxes. The module provides a function `canUnlockAll` that checks if all the boxes in a list of boxes, containing keys (indices) to other boxes, can be unlocked given that the first box is already unlocked.

## Requirements

- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Usage

```python
#!/usr/bin/python3
from lockboxes import canUnlockAll

# Example usage
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
```

## Files

- **0-lockboxes.py**: The main Python module containing the `canUnlockAll` function.
- **main_0.py**: Example script demonstrating the usage of the `canUnlockAll` function.

## Author

- Carrie Ybay, Software Engineer at Holberton School

## Project Timeline

- Project Start: Dec 4, 2023, 6:00 AM
- Checker Released: Dec 5, 2023, 6:00 AM
- Auto Review Deadline: Dec 8, 2023, 6:00 AM

## License

This project is licensed under the [MIT License](LICENSE).
