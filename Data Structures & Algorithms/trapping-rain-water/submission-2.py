class Solution:
    def lrElem(self, idx: int,height: List[int])->List[int]:
        left=-1
        right=-1
        temp=idx
        if idx>0 and idx<len(height)-1:
            while temp>=0:
                if height[temp]>left:
                    left=height[temp]
                temp -= 1
            temp=idx
            while temp<len(height):
                if height[temp]>right:
                    right=height[temp]
                temp += 1
        return [left,right]

            

    def trap(self, height: List[int]) -> int:
        n=len(height)
        water=0
        for i in range(n):
            lr=self.lrElem (i,height)
            left=lr[0]
            right=lr[1]
            #print(left,right)
            if left==-1 or right==-1:
                water+=0
            else:
                water+=min(left,right)-height[i]
        return water
        


        