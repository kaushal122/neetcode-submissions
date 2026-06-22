class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        current_combo=[]
        current_sum=0
        def backtrack(start, current_combo, current_sum):

            if current_sum==target:
                return res.append(current_combo[:])

            if current_sum>target:
                return
            
            for i in range(start,len(nums)):
                current_combo.append(nums[i])
                current_sum+=nums[i]
                backtrack(i,current_combo,current_sum)
                current_combo.pop()
                current_sum-=nums[i]
                
        backtrack(0,current_combo,current_sum)
        return res