
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

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


    print(traverse(root))

if __name__ == "__main__":
    main()
