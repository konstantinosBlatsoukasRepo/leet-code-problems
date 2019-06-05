# Definition for a binary tree node.


class Solution:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
            
        
        