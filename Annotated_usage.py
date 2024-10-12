from typing import Annotated

def validate_positive(value: int) -> int:
    if value <= 0:
        raise ValueError("Value must be positive")
    return value

def process_data(data: Annotated[int, validate_positive]):
    return data

# Usage
try:
    print(process_data(10))  # Works fine
    print(process_data(-5))  # Raises ValueError
except ValueError as e:
    print(e)
