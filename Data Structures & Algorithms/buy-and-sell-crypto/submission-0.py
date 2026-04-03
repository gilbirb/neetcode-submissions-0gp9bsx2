class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        postMax = [0] * length
        postMax[-1] = prices[-1]
        for i in range(length - 2, -1, -1):
            postMax[i] = max(postMax[i + 1], prices[i])

        ans = 0
        for i in range(length - 1):
            profit = postMax[i + 1] - prices[i]
            ans = max(profit, ans)

        return ans