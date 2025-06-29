import pytest
from app.palindrome_check import palindrome_check

"""
Test with valid test cases
1. [Part of data given in question] "Was it a car or a cat I saw?"
2. [Part of data given in question] "!?" // Treated as empty string after trimming
3. "RacECar" // Mix case inbtween string
4. "12321" // All number
5. "a" // Single char
"""
@pytest.mark.parametrize("s", [
    "Was it a car or a cat I saw?",
    "!?",
    "RacECar",
    "12321",
    "a"
])
def test_valid_palindromes(s):
    assert palindrome_check(s) is True

"""
Test with invalid test cases
1. [Part of data given in question] "Hello World"
2. "Not a palindrome!"
3. "abc123"
"""
@pytest.mark.parametrize("s", [
    "Hello World",
    "Not a palindrome!",
    "abc123"
])
def test_invalid_palindromes(s):
    assert palindrome_check(s) is False
    
"""
Test with invalid inputs
1. "" // Empty string, input length > 1
2. "a" * 2001 // Input length < 2 * 10^3
"""
@pytest.mark.parametrize("s", [
    "",
    "a" * 2001,
])
def test_input_length_validation(s):
    long_input = "a" * 2001
    with pytest.raises(Exception):
        palindrome_check(s)