import pytest
import calculator
from calculator import *
from pytest import approx

# handles addition
def test_addition():
  result = add (3,4)
  assert result == 7

# handles subtraction
def test_subtraction():
  assert subtract(3, 4) == -1

# handles multiplication
def test_multiply():
  assert multiply(3, 4) == 12

# handles division
# DONE: handles zero division 
def test_divide():
  assert divide(3, 0) == "Cannot divide by 0"
  assert divide(3, 4) == 3/4
  assert divide(12,3) == 4

def test_get_num(monkeypatch):
  # Mock user input for valid integer
  monkeypatch.setattr('builtins.input', lambda _: "37")
  assert get_num("Enter a number: ") == 37

  # Mock user input for invalid input (non-integer)
  monkeypatch.setattr('builtins.input', lambda _: "a2z")
  assert get_num(
      "Enter a number: ") == "Please enter a valid integer"

def test_get_selection(monkeypatch):
    # Mock user input for valid selection
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_selection() == 1

    # Mock user input for invalid selection
    monkeypatch.setattr('builtins.input', lambda _: "a2z")
    with pytest.raises(ValueError):
        get_selection()

# Handles division by a negative number
def test_divide_negative():
  assert divide(100, -2) == -50
  assert divide(-100, -2) == 50
  assert divide(-100, 2) == -50

# Handles division by a positive number
def test_divide_positive():
  assert divide(12, 3) == 4

# Handles division by a floating-point number
def test_divide_float():
  assert divide(100, 3) == 100/3

# Handles division by zero with negative dividend
def test_divide_zero_negative():
  assert divide(-100, 0) == "Cannot divide by 0"

# Handles division by zero with positive dividend
def test_divide_zero_positive():
  assert divide(100, 0) == "Cannot divide by 0"

# Tests that multiplying two positive numbers works correctly.
def test_multiply_positive_numbers():

  # Arrange
  number_1 = 100
  number_2 = 5
  expected_result = 500

  # Act
  result = multiply(number_1, number_2)

  # Assert
  assert result == expected_result

# Tests that multiplying two negative numbers works correctly.
def test_multiply_negative_numbers():
  # Arrange
  number_1 = -100
  number_2 = -2
  expected_result = 200

  # Act
  result = multiply(number_1, number_2)

  # Assert
  assert result == expected_result


# Gets a selection from user input with valid range
def test_get_selection_valid_range(monkeypatch):
  # Mock user input for valid selection
  monkeypatch.setattr('builtins.input', lambda _: "4")
  assert get_selection() == 4

# Gets a selection from user input with invalid range
def test_get_selection_invalid_range(monkeypatch):
  # Mock user input for valid selection
  monkeypatch.setattr('builtins.input', lambda _: "5")
  with pytest.raises(ValueError):
      get_selection()

  # Mock user input for invalid selection
  monkeypatch.setattr('builtins.input', lambda _: "a2z")
  with pytest.raises(ValueError):
      get_selection()

# Handles division by zero with zero dividend
def test_divide_zero_zero():
  assert divide(1237, 0) == "Cannot divide by 0"
  
  
@pytest.mark.parametrize("num1,num2,expectedResult", [(1, 2, 3), (-1, -2, -3), (1, -2, -1)])
def test_param_add(num1, num2, expectedResult):
    result = calculator.add(num1, num2)
    assert result == expectedResult

# Testing Multiply Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(1, 2, 2), (-1, -2, 2), (1, -2, -2), (3, 7, 21), (7, 7, 49)])
def test_Multiply(num1, num2, expectedResult):
    result = calculator.multiply(num1, num2)
    assert result == expectedResult

# Testing Division Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(49, 7, 7), (-49, -7, 7), (-49, 7, -7)])
def test_Divide(num1, num2, expectedResult):
    result = calculator.divide(num1, num2)
    assert result == expectedResult

# Test Calculator when double 0 values entered
def test_doubleZeroInput():
    result = calculator.subtract(0, 0)
    assert result == 0
