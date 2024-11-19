from sol import Solution, TreeNode

def test_sum_numbers():
    solution = Solution()

    # Test case 1: Single node tree
    root1 = TreeNode(1)
    assert solution.sumNumbers(root1) == 1

    # Test case 2: Tree with multiple nodes
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    # Paths: 12, 13 -> Sum: 12 + 13 = 25
    assert solution.sumNumbers(root2) == 25

    # Test case 3: Tree with more complex structure
    root3 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    # Paths: 495, 491, 40 -> Sum: 495 + 491 + 40 = 1026
    assert solution.sumNumbers(root3) == 1026

    # Test case 4: Empty tree
    root4 = None
    assert solution.sumNumbers(root4) == 0

    # Test case 5: Tree with only left children
    root5 = TreeNode(1, TreeNode(2, TreeNode(3)))
    # Path: 123 -> Sum: 123
    assert solution.sumNumbers(root5) == 123

    # Test case 6: Tree with only right children
    root6 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    # Path: 123 -> Sum: 123
    assert solution.sumNumbers(root6) == 123
