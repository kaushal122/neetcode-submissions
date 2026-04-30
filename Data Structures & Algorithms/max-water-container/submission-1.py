class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1=0
        ptr2=len(heights)-1
        result=0
        while ptr1<ptr2:
            l=min(heights[ptr1],heights[ptr2])
            w=ptr2-ptr1
            area=l*w
            print(area)
            result=max(area,result)
            if heights[ptr2]<heights[ptr1]:
                ptr2 -= 1
            else:
                ptr1 += 1

        return result
