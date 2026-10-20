class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def solve(idx:int,su:int):
            if su==amount:
                return 0
            elif idx>=n or su>amount:
                return float('inf')
            
            elif dp[idx][su]!=-1:
                return dp[idx][su]

            take= 1+solve(idx,su+coins[idx])

            skip=solve(idx+1,su)
            dp[idx][su]=min(take,skip)
            return dp[idx][su]
        result = solve(0, 0)
        
        # If result is still infinity, it means the amount cannot be formed
        return result if result != float('inf') else -1