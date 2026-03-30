class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        totalZeros = 0
        for num in nums:
            if num == 0:
                totalZeros += 1
                continue
            totalProd *= num

        if totalZeros == len(nums):
            return nums

        for i in range(len(nums)):
            if totalZeros:
                if nums[i] == 0:
                    if totalZeros > 1:
                        nums[i] = 0
                    else:
                        nums[i] = totalProd
                else:
                    nums[i] = 0
            else:
                nums[i] = totalProd // nums[i]

        return nums