# openswe-test

A simple Python project to provide and test openswe integration.

## Features

- Basic arithmetic functions: add, subtract, multiply, divide
- Power functions: square, cube

## Usage

```python
from calculator import add, subtract, multiply, divide, square, cube

result = add(2, 3)       # 5
result = subtract(5, 3)  # 2
result = multiply(3, 4)  # 12
result = divide(10, 2)   # 5.0
result = square(4)       # 16
result = cube(3)         # 27
```

## Running Tests

```bash
pytest test_calculator.py
```
