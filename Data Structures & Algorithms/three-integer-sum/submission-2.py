class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        hm = {}
        length = len(nums)
        for i in range(length - 2):
            num = nums[i]
            if num in hm:
                continue
            p1 = i + 1
            p2 = length - 1
            target = -num
            while p1 < p2:
                _sum = nums[p1] + nums[p2]
                if _sum == target:
                    j = nums[p1]
                    k = nums[p2]
                    ans.append([num, j, k])
                    while p1 < length and j == nums[p1]:
                        p1 += 1
                    while p2 >= 0 and k == nums[p2]:
                        p2 -= 1
                elif _sum < target:
                    p1 += 1
                else:
                    p2 -= 1
            hm[num] = 1
        return ans