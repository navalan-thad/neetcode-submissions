class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def countFreq(s):
            count = {}
            for i in s:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            return count

        s1_freq = countFreq(s1)
        print(f"s1 freq: {s1_freq}")
            

        start = 0
        end = len(s1)
        count = countFreq(s2[start:end])

        while end < len(s2):
            if count == s1_freq:
                return True
            else:
                count[s2[start]] -= 1
                if count[s2[start]] == 0:
                    del count[s2[start]]
                if s2[end] in count:
                    count[s2[end]] += 1
                else:
                    count[s2[end]] = 1

            start += 1
            end += 1

        if count == s1_freq:
            return True

        return False


        