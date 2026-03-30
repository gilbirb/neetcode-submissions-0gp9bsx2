class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                ans = map[diff]
                if ans == i:
                    continue
                if ans < i:
                    return [ans, i]
                else:
                    return [i, ans]
        return [-1,-1]