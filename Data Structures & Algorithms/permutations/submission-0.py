class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        used = {}

        def rec(cur):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return

            for num in nums:
                if num not in used:
                    used[num] = True
                    cur.append(num)
                    rec(cur)
                    cur.pop()
                    del used[num]

        rec([])
        return ans