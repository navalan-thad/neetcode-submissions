class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m-1
        p2 = n-1
        i = len(nums1) - 1
        while i >= 0:
            if p1 < 0:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                if nums2[p2] > nums1[p1]:
                    nums1[i] = nums2[p2]
                    p2 -= 1
                else:
                    nums1[i] = nums1[p1]
                    p1 -= 1
            i -= 1

            
        