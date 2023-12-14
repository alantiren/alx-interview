# Pascal's Triangle

## Description

This Python module provides a function to generate Pascal's Triangle up to a specified number of rows.

## Installation

No special installation is required. Simply include the `0-pascal_triangle.py` file in your project.

## Usage

```python
from 0-pascal_triangle import pascal_triangle

# Example usage
result = pascal_triangle(5)
print(result)
```

## Function: `pascal_triangle(n)`

Generates Pascal's Triangle up to the nth row.

### Parameters

- `n`: An integer representing the number of rows in Pascal's Triangle.

### Returns

A list of lists of integers representing Pascal's Triangle.

If `n` is less than or equal to 0, an empty list is returned.

## Example

```python
from 0-pascal_triangle import pascal_triangle

# Example usage
result = pascal_triangle(5)
print(result)
```

Output:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## License

This project is licensed under the [MIT License](LICENSE).

```