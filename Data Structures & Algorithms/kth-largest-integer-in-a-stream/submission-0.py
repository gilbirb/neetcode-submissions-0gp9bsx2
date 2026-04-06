class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.pq = nums
        self.k = k
        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        length = len(self.pq)
        if length > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]