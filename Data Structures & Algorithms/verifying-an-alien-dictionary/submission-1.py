class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        rank = {char: index for index, char in enumerate(order)}
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            minlen = min(len(word1), len(word2))
            if word1[0:minlen] == word2[0:minlen]:
                if len(word1) > len(word2):
                    return False
            else:
                for j in range(minlen):
                    if rank[word1[j]] < rank[word2[j]]:
                        break
                    elif rank[word1[j]] > rank[word2[j]]:
                        return False
            
        return True
        