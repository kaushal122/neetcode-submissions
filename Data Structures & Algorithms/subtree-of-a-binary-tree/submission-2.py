# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:  
    def isSameTree(self,root:TreeNode,subRoot:TreeNode)->bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        return root.val==subRoot.val and self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right) 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if  root is None:
            return False
        if self.isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        