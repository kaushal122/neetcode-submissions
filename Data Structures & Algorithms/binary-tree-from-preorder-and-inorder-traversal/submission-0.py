# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp={}
        idx=[0]
        for i in range(len(inorder)):
            mp[inorder[i]]=i
        

        def  solve(left:int,right:int) -> Optional[TreeNode]:

            if left>right:
                return None

            
            root=TreeNode(preorder[idx[0]])
            mid=mp[preorder[idx[0]]]
            idx[0]+=1            

            root.left=solve(left,mid-1)
            root.right=solve(mid+1,right)
            
            return root

        return solve(0,len(preorder)-1)

        
        