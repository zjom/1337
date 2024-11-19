# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def aux(node: TreeNode | None) -> TreeNode | None:
            if not node:
                return None

            # Flatten left and right subtrees
            left_tail = aux(node.left)
            right_tail = aux(node.right)

            # If there is a left subtree, attach it to the right
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None  # Set left to None

            # Return the tail of the flattened subtree
            return right_tail if right_tail else left_tail if left_tail else node

        _ = aux(root)
        return

def traverse(node: TreeNode|None)->list[int]:
    if not node:
        return []

    res:list[int] = []
    res.append(node.val)

    res.extend(traverse(node.left))
    res.extend(traverse(node.right))
    return res

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(7)

    Solution().flatten(root)

    print(traverse(root))

if __name__ == "__main__":
    main()
