from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = dict()

        for i in strs:
            string = "".join(sorted(i))
            if string in result:
                result[string].append(i)
            else:
                result[string] = [i]

        return list(result.values())
        