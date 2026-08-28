import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def bs(left, right):
            while left <= right:
                mid = (left + right) // 2
                if x < arr[mid]:
                    right = mid - 1
                elif x > arr[mid]: 
                    left = mid + 1
                else:
                    return mid

            if left >= len(arr):
                return len(arr) - 1
            if left > 0 and abs(arr[left - 1] - x) <= abs(arr[left] - x):
                return left - 1
            return left

        start = bs(0, len(arr)-1)
        end = start

        while end - start + 1 < k:
            if start > 0 and end + 1 < len(arr):
                if abs(arr[start - 1]-x) <= abs(arr[end + 1]-x):
                    start -= 1
                else:
                    end += 1
            elif start > 0:
                start -= 1
            else:
                end += 1

        return arr[start:end+1]

