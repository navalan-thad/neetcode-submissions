class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = []
        freqCount = {}
        for i in nums: 
            if i in freqCount:
                freqCount[i] += 1
            else:
                freqCount[i] = 1

        res = []
        for k, v in freqCount.items():
            if v > len(nums) // 3:
                res.append(k)

        return res

        