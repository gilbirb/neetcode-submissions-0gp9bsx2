class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        
        def rec(cur, potential, index):
            if cur > target:
                return
            elif cur == target:
                ans.append(potential[:])
                return

            for i in range(index, len(nums)):
                num = nums[i]
                potential.append(num)
                rec(cur + num, potential, i)
                potential.pop()

        rec(0, [], 0)
        return ans


            