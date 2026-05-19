class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=lambda x: len(x))
        smallest = strs[0]

        def findPrefix():
            prefix = 0
            for i in range(len(smallest)):
                for s in strs:
                    if s[i] != smallest[i]:
                        return prefix
                prefix += 1

            return prefix

        prefix = findPrefix()
        if prefix == -1:
            return ""
        return smallest[:prefix]


        

            


        