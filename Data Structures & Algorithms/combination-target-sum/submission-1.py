class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        
        def rec(cur, potential):
            if cur > target:
                return
            elif cur == target:
                sorted_cur = sorted(potential)
                if sorted_cur not in ans:
                    ans.append(sorted_cur)
                return

            for num in nums:
                potential.append(num)
                rec(cur + num, potential)
                potential.pop()

        rec(0, [])
        return ans

            