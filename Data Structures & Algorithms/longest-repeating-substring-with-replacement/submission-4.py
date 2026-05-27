class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        end = 1
        maxSub = 1
        maxFreq = {s[start]: 1}

        while end < len(s):
            if s[end] in maxFreq:
                maxFreq[s[end]] += 1
            else:
                maxFreq[s[end]] = 1

            size = end - start + 1
            if size - max(maxFreq.values()) <= k:
                maxSub = max(maxSub, size)
            else:
                maxFreq[s[start]] -= 1
                start += 1
            end += 1

        return maxSub

        


        

        
        