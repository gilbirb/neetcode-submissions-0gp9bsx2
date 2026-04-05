class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        
        def rec(i, cur):
            if i >= length:
                ans.append(cur[:])
                return

            cur.append(nums[i])
            rec(i + 1, cur)
            cur.pop()
            rec(i + 1, cur)

        rec(0, [])
        return ans
        