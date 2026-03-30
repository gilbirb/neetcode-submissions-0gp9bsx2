class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = False;

        for i in range(len(nums)):
            if (map[nums[i]] == False):
                map[nums[i]] = True
            else:
                return True
        return False
