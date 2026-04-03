class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        ans = 0
        for price in prices:
            lowest = min(lowest, price)
            profit = price - lowest
            ans = max(profit, ans)
        return ans