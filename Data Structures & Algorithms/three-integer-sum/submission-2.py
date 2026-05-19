class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()
        nums.sort()

        for i in range(len(nums)):
            start = i+1
            end = len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    result.add(tuple([nums[i], nums[start], nums[end]]))
                    start += 1
                    end -= 1
        
        return list(result)