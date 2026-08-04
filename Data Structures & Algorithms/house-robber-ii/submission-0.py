class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        def rob_linear(houses:List[int])->int:

            memo={}

            def solve(i:int)->int:
                if i>=len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i]=max(houses[i]+solve(i+2),solve(i+1))
                return memo[i]
            
            return solve(0)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
            