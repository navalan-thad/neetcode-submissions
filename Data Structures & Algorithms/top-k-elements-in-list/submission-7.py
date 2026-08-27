import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for _ in range(len(nums)+1)]

        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for key, v in freq.items():
            buckets[v].append(key)

        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)

                if len(res) == k:
                    return res

        return []
