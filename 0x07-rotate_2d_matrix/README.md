# 0x07 Rotate 2D Matrix

This project contains a Python script that rotates an n x n 2D matrix 90 degrees clockwise.

## Getting Started

These instructions will help you run the script and see the rotated matrix.

### Prerequisites

- Python 3.x

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/alantiren/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-interview/0x07-rotate_2d_matrix
   ```

3. Run the script:

   ```bash
   ./0-rotate_2d_matrix.py
   ```

   The script will rotate the provided matrix and print the result.

## Example

```python
#!/usr/bin/python3

from 0-rotate_2d_matrix import rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

The above example initializes a 3x3 matrix and rotates it using the `rotate_2d_matrix` function.


## Acknowledgments

- This script was created as part of an interview preparation project.
- Thanks to ALX Software Engineering School.
