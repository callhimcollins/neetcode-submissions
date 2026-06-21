# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSame(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)
        
        def isSub(node):
            if not node:
                return False
            if checkSame(node, subRoot):
                return True
            return isSub(node.left) or isSub(node.right)
        
        return isSub(root)