class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lb = max(weights)
        ub = sum(weights)

        def deliveryTime(cap):
            days_taken = 0
            curr_weight = 0
            for i in range(len(weights)):
                if curr_weight + weights[i] > cap:
                    days_taken += 1
                    curr_weight = weights[i]
                else:
                    curr_weight += weights[i]

            return days_taken


        while lb <= ub:
            mid = (lb + ub) // 2
            if deliveryTime(mid) < days:
                ub = mid-1
            else:
                lb = mid+1

        return lb