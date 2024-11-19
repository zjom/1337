import pytest
from sol1 import Solution

@pytest.mark.parametrize("input, expected", [
    ("1+1", 2),
    (" 2-1 + 2 ", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),
])
def test_sol(input: str, expected: int):
    assert Solution().calculate(input) == expected

