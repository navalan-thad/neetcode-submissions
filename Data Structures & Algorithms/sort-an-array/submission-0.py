class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid

            tempLeft = [0] * n1
            tempRight = [0] * n2

            for i in range(n1):
                tempLeft[i] = arr[left+i]

            for j in range(n2):
                tempRight[j] = arr[mid+1+j]

            i, j = 0, 0
            k = left

            while i < n1 and j < n2:
                if tempLeft[i] <= tempRight[j]:
                    arr[k] = tempLeft[i]
                    i += 1
                else:
                    arr[k] = tempRight[j]
                    j += 1
                k += 1

            while i < n1:
                arr[k] = tempLeft[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = tempRight[j]
                j += 1
                k += 1


        def mergeSort(arr, left, right):
            if left >= right:
                return arr

            mid = (left + right) // 2

            mergeSort(arr, left, mid)
            mergeSort(arr, mid+1, right)
            merge(arr, left, mid, right)

            return arr

        return mergeSort(nums, 0, len(nums)-1)
            
        