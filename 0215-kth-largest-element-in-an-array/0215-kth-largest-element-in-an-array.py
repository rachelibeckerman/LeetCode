import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        i = 0
        while i < k-1:
            heapq._heappop_max(nums)
            i += 1
        return heapq._heappop_max(nums)
        