import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap1=[]
        self.k=k
        for num in nums:
            heapq.heappush(self.heap1,num)
        while len(self.heap1)>k:
            heapq.heappop(self.heap1)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap1,val)
        if len(self.heap1)>self.k:
            heapq.heappop(self.heap1)
        return self.heap1[0]

    
        
