# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def height(self, root:TreeNode) -> int:
        if root is None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        h1=0
        h2=0
        if root.left:
            h1=self.height(root.left)
        if root.right:
            h2=self.height(root.right)
        #print(h1,h2)

        return max(h1+h2,self.diameterOfBinaryTree(root.left),
                    self.diameterOfBinaryTree(root.right))
        