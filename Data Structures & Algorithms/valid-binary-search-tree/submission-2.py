# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mn=-1001
        mx=1001
        return self.solve(root,mn,mx)
    
    def solve(self, root:TreNode, mn:int, mx:int) -> bool:
        if root is None:
            return True
        if root.val<=mn or root.val>=mx:
            return False
        
        return self.solve(root.left,mn,root.val) and self.solve(root.right,root.val,mx)

    
        