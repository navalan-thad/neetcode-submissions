class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1, count2, cand1, cand2 = 0, 0, 0, 0
        res = []

        for i in nums:
            if i == cand1:
                count1 += 1
            elif i == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = i
                count1 = 1
            elif count2 == 0:
                cand2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > len(nums) // 3:
                res.append(cand)

        return res

        