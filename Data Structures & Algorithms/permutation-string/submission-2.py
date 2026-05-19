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

        while end <= len(s2):
            count = countFreq(s2[start:end])
            print(count)
            if count == s1_freq:
                return True
            start += 1
            end += 1

        return False


        