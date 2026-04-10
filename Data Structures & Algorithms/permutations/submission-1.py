class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        used = set()

        def rec(cur):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    cur.append(num)
                    rec(cur)
                    cur.pop()
                    used.discard(num)

        rec([])
        return ans