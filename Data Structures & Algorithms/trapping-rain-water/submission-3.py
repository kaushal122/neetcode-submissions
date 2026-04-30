class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[-1]*n
        right=[-1]*n
        temp=0
        lh=-1
        while temp<n:
            if temp==0 or height[temp]>=lh:
                lh=height[temp]
                left[temp]=-1
            else:
                left[temp]=lh
            temp +=1
        #print(left)
        temp=n-1
        rh=-1
        while temp>=0:
            if temp==n-1 or height[temp]>=rh:
                rh=height[temp]
                right[temp]=-1
            else:
                right[temp]=rh
            temp-=1
        #print(right)
        water=0
        for i in range(n):
            if left[i]!=-1 and right[i]!=-1:
                temp=min(right[i],left[i])-height[i]
                #print(temp)
                water+=temp
        return water