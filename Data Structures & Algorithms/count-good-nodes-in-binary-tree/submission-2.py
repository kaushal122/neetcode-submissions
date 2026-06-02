# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:        

    def goodNodes(self, root: TreeNode) -> int:
        self.total=0
        lowest_value = float('-inf')
        self.Solve(root,lowest_value)
        return self.total

    def Solve(self, root: TreeNode, m1:int) -> None:
        if root is None:
            return 
        if root.val>=m1:
            self.total +=1
            self.Solve(root.left,root.val)
            self.Solve(root.right,root.val)
        else:
            self.Solve(root.left,m1)
            self.Solve(root.right,m1)
        return