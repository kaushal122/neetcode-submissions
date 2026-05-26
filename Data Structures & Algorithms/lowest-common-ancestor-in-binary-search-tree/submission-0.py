# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower=p.val if p.val<q.val else q.val
        high=p.val if p.val>q.val else q.val

        if root.val>=lower and root.val<high or root.val>lower and root.val<=high:
            return root
        elif root.val>lower and root.val>high:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)