class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(min_heap, nums[i])

        return min_heap[0]