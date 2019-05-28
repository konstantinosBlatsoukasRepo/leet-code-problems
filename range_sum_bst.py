"""
number 938
binary search tree
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        root_val = root.val if L <= root.val <= R else 0
        return root_val+self.rangeSumBST(root.left, L, R)+self.rangeSumBST(root.right, L, R)
