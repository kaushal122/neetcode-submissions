class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h=0
        width=0
        n=len(heights)
        result=0
        for i in range(n):
            j=i+1
            while j<n:
                width=j-i
                h=min(heights[i],heights[j])
                area=h*width
                result=max(area,result)
                j += 1
        return result

        