import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            top1 = max(stones)
            stones.remove(top1)
            top2 = max(stones)
            stones.remove(top2)

            if top1 != top2:
                stones.append(abs(top1 - top2))

        if len(stones) == 1:
            return stones[0]
        return 0



        