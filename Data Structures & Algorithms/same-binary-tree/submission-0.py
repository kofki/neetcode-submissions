# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(p, q):
            if p and not q:
                return False
            if q and not p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            return inorder(p.left, q.left) and inorder(p.right, q.right)
        return inorder(p, q)
        
                