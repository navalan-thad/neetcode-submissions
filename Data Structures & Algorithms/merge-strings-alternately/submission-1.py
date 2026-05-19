class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []

        minlen = min(len(word1), len(word2))

        for i in range(minlen):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > len(word2):
            remaining = len(word1) - minlen
            result.append(word1[-remaining:])
        elif len(word2) > len(word1):
            remaining = len(word2) - minlen
            result.append(word2[-remaining:])

        return "".join(result)

        

        