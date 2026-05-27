# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        queue.append(root)
        if not root:
            return []
        res=[]
        while queue:
            s=len(queue)
            while(s):
                temp=queue.popleft()
                if s==1:
                    res.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                s-=1
        return res
            


        