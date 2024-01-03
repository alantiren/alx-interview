# UTF-8 Validation

This project involves implementing a Python function to determine if a given data set represents a valid UTF-8 encoding.

## Project Overview


## Project Files

- **Main Implementation:** [0-validate_utf8.py](0x04-utf8_validation/0-validate_utf8.py)
- **Test Script:** [0-main.py](0x04-utf8_validation/0-main.py)

## Project Requirements

- **Allowed Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Endings:** All files should end with a new line
- **Shebang:** The first line of all your files should be exactly `#!/usr/bin/python3`
- **README.md:** A README.md file at the root of the project folder is mandatory
- **Coding Style:** Use PEP 8 style (version 1.7.x)
- **Executable Files:** All files must be executable

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-interview/0x04-utf8_validation
   ```

3. Run the test script:

   ```bash
   ./0-main.py
   ```

## Function Description

The `validUTF8` function in [0-validate_utf8.py](0x04-utf8_validation/0-validate_utf8.py) checks if a given list of integers represents a valid UTF-8 encoding.

### Function Signature

```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Function implementation
```

## Example Usage

```python
# Example usage in 0-main.py
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Additional Resources

- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
