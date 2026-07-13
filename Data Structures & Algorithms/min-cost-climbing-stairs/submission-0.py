class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)  
        def RunStep(idx:int):
            if idx>=n:
                return 0
            elif dp[idx]!=-1:
                print(idx)
                return dp[idx]
            else:
                dp[idx]=min(cost[idx]+RunStep(idx+1),cost[idx]+RunStep(idx+2))
                return dp[idx]
        
        res=min(RunStep(0),RunStep(1))

        return res