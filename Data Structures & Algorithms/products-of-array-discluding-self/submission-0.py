class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        right=[0]*n
        left=[0]*n

        last=1
        for i in range(len(nums)):
            left[i]=last*nums[i]
            last=left[i]
       # print(left)
        last=1
        for j in range(len(nums)-1,0,-1):
            right[j]=last*nums[j]
            last=right[j]
        #print(right)
        res=[0]*n
        for i in range(n):
            if i==0:
                res[i]=right[i+1]
            elif i==n-1:
                res[i]=left[i-1]
            else:
                res[i]=left[i-1]*right[i+1]

        return res
        


        