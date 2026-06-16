class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[] #max heap
        for num in nums:
            #print(num)
            heapq.heappush(heap,1*num)
            if len(heap)>k:
                heapq.heappop(heap)
            #print(heap[0])
        return 1*heap[0]

        
        