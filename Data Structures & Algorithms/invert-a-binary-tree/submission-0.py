# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def solve(self, root:TreeNode)->TreeNode:
        if root==None:
            return 
        temp=root.left
        # if temp:
        #     print(temp.val)
        root.left=root.right
        # if root.left:
        #     print(root.left.val)
        root.right=temp

        self.solve(root.left)
        self.solve(root.right)

        return
        

        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy=root
        self.solve(root)

        return dummy
        

        
        