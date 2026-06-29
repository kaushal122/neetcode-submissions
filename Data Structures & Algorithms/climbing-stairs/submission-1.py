class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def dpSolve(n:int):
            if n==0:
                return 1
            elif n<0:
                return 0
            elif dp[n] != -1:
                return dp[n]
            
            dp[n]=dpSolve(n-1)+dpSolve(n-2)
            return dp[n]
        
        ways=dpSolve(n)

        return ways

