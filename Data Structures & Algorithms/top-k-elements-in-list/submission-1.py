class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        temp=[[] for i in range(len(nums)+1)]

        for n in nums:
            freq[n]= 1+freq.get(n,0)
        for n,c in freq.items():
            temp[c].append(n)
        ans=[]
        for i in range(len(temp)-1,0,-1):
            for n in temp[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans