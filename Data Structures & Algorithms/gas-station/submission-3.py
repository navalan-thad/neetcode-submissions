class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = 0       # total net gas across all stations
        tank = 0        # current tank while testing a candidate start
        start = 0       # candidate starting station

        for i in range(len(gas)):

            diff = gas[i] - cost[i]

            total += diff
            tank += diff

            # current start cannot reach station i + 1
            if tank < 0:
                start = i + 1
                tank = 0

        # impossible to complete circuit
        if total < 0:
            return -1

        return start