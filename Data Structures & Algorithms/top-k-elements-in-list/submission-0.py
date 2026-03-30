class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqList = list(count.items())
        freqList.sort(reverse=True, key=lambda x: x[1])

        ans = []
        for i in range(0, k):
            ans.append(freqList[i][0])
        return ans