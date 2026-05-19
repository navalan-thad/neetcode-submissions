class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        for i in range(0, len(temperatures)-1):
            curr = temperatures[i]
            j = i+1
            while j < len(temperatures):
                if curr < temperatures[j]:
                    result[i] = j - i
                    break
                j += 1

        return result
        