class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        pre1 = [0] * length
        pre2 = [0] * length
        pre1[0] = height[0]
        pre2[-1] = height[-1]

        for i in range(1, length):
            pre1[i] = max(pre1[i - 1], height[i])

        for i in range(length - 2, -1, -1):
            pre2[i] = max(pre2[i + 1], height[i])

        ans = 0
        for i in range(length):
            ans += (min(pre1[i], pre2[i]) - height[i])

        return ans