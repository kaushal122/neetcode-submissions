class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)

        def getMoney(idx:int):
            if idx>=n:
                return 0
            elif dp[idx]!=-1:
                return dp[idx]
            else:
                dp[idx]=max(nums[idx]+getMoney(idx+2),nums[idx]+getMoney(idx+3))
                return  dp[idx]
        return max(getMoney(0),getMoney(1))
