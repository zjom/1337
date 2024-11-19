from sol import Solution


def test_one():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    assert Solution().spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]

def test_two():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    assert Solution().spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]
