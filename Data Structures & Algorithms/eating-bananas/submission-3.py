import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        piles.sort()
        maxK=piles[-1]
        minK=math.ceil((sum(piles)/h))
        while minK<=maxK:
            time=0
            midK=(minK+maxK+1)//2
            #print("midK",midK)
            for i in range(n):
                time+=(int)(math.ceil(piles[i]/midK))
            #print("time",time)
            if time<=h:
                res=midK
                maxK=midK-1
            elif time>h:
                minK=midK+1
        return res


            
