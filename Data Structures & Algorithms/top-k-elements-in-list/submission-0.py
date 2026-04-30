class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for x in nums:
            freq[x]= freq.get(x,0) + 1
        freq=dict(sorted(freq.items(),key=lambda x:x[1], reverse=True))
        #print(freq)
        lst=list(freq.items())
        for x in range(k):
            key,value=lst[x]
            ans.append(key)
        return list(ans)