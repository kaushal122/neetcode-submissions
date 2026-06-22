class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtrack(idx,curr):
            res.append(curr[:])

            for i in range(idx,len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])

        return res
