from sol import Solution


def test_one():
    s = "paper"
    t = "title"
    assert Solution().isIsomorphic(s,t)

def test_two():
    s = "badc"
    t = "baba"
    assert not Solution().isIsomorphic(s,t)
