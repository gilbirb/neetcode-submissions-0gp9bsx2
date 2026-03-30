class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)

        for n in numSet:
            next = n + 1
            conseq = 1
            while n + 1 in numSet:
                conseq += 1
                n += 1
            ans = max(ans, conseq)

        return ans