class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count=[0]*26
        for task in tasks:
            count[ord(task)-ord("A")]+=1
        heap=[]
        for i in range(26):
            if count[i]:
                heapq.heappush(heap,-1*count[i])
        time=0
        q=deque()

        while heap or q:
            time+=1

            if not heap:
                time=q[0][1]
            else:
                cnt = 1+ heapq.heappop(heap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
        return time

        