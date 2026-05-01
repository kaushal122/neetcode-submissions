class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[0]*n
        right=[0]*n
        stack=[]

        
        for i in range(n):
            if len(stack)==0:
                stack.append(i)
            elif heights[i]>=heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and heights[i]<heights[stack[-1]] :
                    left[stack[-1]]=i-1
                    stack.pop()
                stack.append(i)
        while len(stack)>0:
            left[stack[-1]]=n-1
            stack.pop()
        stack=[]
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                stack.append(i)
            elif heights[i]>=heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and heights[i]<heights[stack[-1]]:
                    right[stack[-1]]=i+1
                    stack.pop()
                stack.append(i)
        while len(stack)>0:
            right[stack[-1]]=0
            stack.pop()
        res=0
       # print(left)
        #print(right)
        for i in range(n):
            length=left[i]-right[i]+1
            height=heights[i]
            #print(length,height)
            area=length*height
            res=max(res,area)
        return res

        