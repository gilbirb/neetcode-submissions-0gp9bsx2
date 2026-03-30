class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        cur = numbers[p1] + numbers[p2]
        while cur != target:
            if cur > target:
                p2 -= 1
            else:
                p1 += 1
            cur = numbers[p1] + numbers[p2]
        return [p1 + 1, p2 + 1]