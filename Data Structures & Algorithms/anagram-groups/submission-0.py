from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = dict()
        for i in strs:
            code = "".join(sorted(i))
            if code in result:
                result[code].append(i)
            else:
                result[code] = [i]

        return list(result.values())
            
        