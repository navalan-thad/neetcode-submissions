class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        target_a, target_b, target_c = False, False, False
        for i in triplets:
            a, b, c = i
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                target_a = True
            if b == target[1]:
                target_b = True
            if c == target[2]:
                target_c = True

        return target_a and target_b and target_c
            



        



        