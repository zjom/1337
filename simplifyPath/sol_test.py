import pytest
from sol import Solution

@pytest.mark.parametrize("path, expected", [
    ("/home/", "/home"),
    ("/home//foo/", "/home/foo"),
    ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
    ("/../", "/"),
    ("/.../a/../b/c/../d/./", "/.../b/d"),
    ("/a/./b/../../c/", "/c")
])
def test_simplifyPath(path:str, expected:str):
    solution = Solution()
    assert solution.simplifyPath(path) == expected
