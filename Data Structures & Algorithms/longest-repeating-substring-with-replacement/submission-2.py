class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        end = 1
        maxSub = 1
        freqCount = {s[start]:1}

        while end < len(s):
            if s[end] in freqCount:
                freqCount[s[end]] += 1
            else:
                freqCount[s[end]] = 1

            size = end - start + 1    
            if size - max(freqCount.values()) <= k:
                maxSub = max(maxSub, size)
                end += 1
            else:
                freqCount[s[start]] -= 1
                start += 1
                end += 1

        return maxSub


        

        
        