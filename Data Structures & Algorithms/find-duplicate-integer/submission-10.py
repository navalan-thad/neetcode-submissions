class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        # advance once
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # loop exits when cycle found
        slow = nums[0] # reset to beginning
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        

        
        