from sol import Solution


def test_one():
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def test_two():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]
