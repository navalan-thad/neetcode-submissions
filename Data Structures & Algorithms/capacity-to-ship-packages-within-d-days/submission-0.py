class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lower = max(weights)
        upper = sum(weights)

        def sim(cap):
            time = 1
            i = 0
            weight = 0
            while i < len(weights):
                if weight + weights[i] <= cap:
                    weight += weights[i]
                else:
                    time += 1
                    weight = weights[i]
                i += 1

            return time
                
        while lower <= upper:
            mid = (lower + upper) // 2
            if sim(mid) <= days:
                upper = mid-1
            else:
                lower = mid+1

        return lower

