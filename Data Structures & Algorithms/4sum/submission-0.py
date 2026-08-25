class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        quads = set()
        nums.sort()

        for i in range(n):
            for j in range(i+1, n):

                temp = target - nums[i] - nums[j]
                p1 = j+1
                p2 = n-1

                while p1 < p2:
                    if nums[p1] + nums[p2] > temp:
                        p2 -= 1
                    elif nums[p1] + nums[p2] < temp:
                        p1 += 1
                    else:
                        quads.add((nums[i],nums[j],nums[p1],nums[p2]))
                        p1 += 1
                        p2 -= 1

        return list(quads)



        