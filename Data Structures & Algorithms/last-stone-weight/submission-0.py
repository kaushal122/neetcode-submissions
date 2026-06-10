class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap1=[]
        for stone in stones:
            heapq.heappush(heap1,-1*stone)
        while len(heap1)>1:
            f1=-1*heapq.heappop(heap1)
            f2=-1*heapq.heappop(heap1)
            f=abs(f1-f2)
            heapq.heappush(heap1,-1*f)
        return -1*heap1[0]
        