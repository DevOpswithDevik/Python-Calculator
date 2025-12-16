# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive():
    """Test standard addition of positive integers."""
    assert add(1, 4) == 5

def test_add_negative():
    """Test addition involving negative integers."""
    assert add(-1, -4) == -5

def test_subtract():
    """Test standard subtraction."""
    assert subtract(10, 5) == 5

def test_multiply():
    """Test standard multiplication."""
    assert multiply(3, 7) == 21

def test_divide_standard():
    """Test standard division."""
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    # We expect the specific ValueError to be raised
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    # Check if the error message is correct
    assert 'Cannot divide by zero!' in str(excinfo.value)