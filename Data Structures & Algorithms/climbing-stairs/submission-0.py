class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n + 1)
        
        def rec(remaining):
            if remaining < 0:
                return 0
            if dp[remaining] != -1:
                return dp[remaining]
            if remaining == 0:
                return 1

            dp[remaining] = rec(remaining - 2) + rec(remaining - 1)
            return dp[remaining]

        rec(n)
        return dp[n] 
        