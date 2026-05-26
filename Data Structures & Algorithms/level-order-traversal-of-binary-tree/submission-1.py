# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        if not root:
            return []
        res=[]
        while queue:
            s=len(queue)
            l1=[]
            while(s):
                temp=queue.popleft()
                l1.append(temp.val)
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                s-=1
            res.append(l1)
            
        return res

        