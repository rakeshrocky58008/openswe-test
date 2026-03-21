# openswe-test

A simple Python calculator module for testing [OpenSWE](https://github.com/rakeshrocky58008/openswe-test) integration. It provides common arithmetic and power functions with full test coverage.

## Features

- **Arithmetic operations** — `add`, `subtract`, `multiply`, `divide`
- **Power functions** — `square`, `cube`
- **Error handling** — raises `ValueError` on division by zero
- **Fully tested** — comprehensive test suite using `pytest`

## Requirements

- Python 3.7+
- [pytest](https://docs.pytest.org/) (for running tests)

## Getting Started

Clone the repository and install the test dependency:

```bash
git clone https://github.com/rakeshrocky58008/openswe-test.git
cd openswe-test
pip install pytest
```

## Usage

```python
from calculator import add, subtract, multiply, divide, square, cube

add(2, 3)         # 5
subtract(5, 3)    # 2
multiply(3, 4)    # 12
divide(10, 2)     # 5.0
square(4)         # 16
cube(3)           # 27
```

### Division by Zero

`divide` raises a `ValueError` when the divisor is zero:

```python
divide(5, 0)  # raises ValueError: Cannot divide by zero
```

## API Reference

| Function     | Parameters | Returns                  |
| ------------ | ---------- | ------------------------ |
| `add`        | `a, b`    | Sum of `a` and `b`      |
| `subtract`   | `a, b`    | Difference `a - b`      |
| `multiply`   | `a, b`    | Product of `a` and `b`  |
| `divide`     | `a, b`    | Quotient `a / b` (float)|
| `square`     | `a`       | `a` squared             |
| `cube`       | `a`       | `a` cubed               |

## Running Tests

```bash
pytest test_calculator.py
```

## License

This project is available under the [MIT License](LICENSE).
