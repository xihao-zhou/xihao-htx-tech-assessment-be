import pytest
from app.num_palindrome_check import num_palindrome_check

"""
Test with valid test cases
1. [Part of data given in question] 121
2. 123454321
3. 43211234
4. 1
5. 0
"""
@pytest.mark.parametrize("x", [
    121,
    123454321,
    43211234,
    1,
    0
])
def test_valid_palindromes(x):
    assert num_palindrome_check(x) is True

"""
Test with invalid test cases
1. [Part of data given in question] -121
2. [Part of data given in question] -10
3. 10
4. 123
5. 123456789
"""
@pytest.mark.parametrize("x", [
    -121,
    123,
    10,
    123456789
])
def test_invalid_palindromes(x):
    assert num_palindrome_check(x) is False

"""
Test with invalid inputs
1. 2**31 // Too large
2. -2**31 - 1 // Too small
"""
@pytest.mark.parametrize("x", [
    2**31,
    -2**31 - 1
])
def test_input_length_validation(x):
    with pytest.raises(ValueError):
        num_palindrome_check(x)

"""
Test with invalid inputs types
1. "aba" // string
2. 121.0 // float
3. None // None type
4. [] // list
5. True // boolean
"""
@pytest.mark.parametrize("x", [
    "aba",
    121.0,
    None,
    [],
    True
])
def test_invalid_types_raise(x):
    with pytest.raises(TypeError):
        num_palindrome_check(x)