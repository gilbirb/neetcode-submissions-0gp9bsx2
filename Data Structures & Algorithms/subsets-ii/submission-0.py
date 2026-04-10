class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        def rec(cur, i):
            if i >= len(nums):
                ans.append(cur.copy())
                return

            cur.append(nums[i])
            rec(cur, i + 1)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            rec(cur, i + 1)

        rec([], 0)
        return ans