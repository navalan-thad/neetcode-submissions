class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        listS = list(s)
        listT = list(t)

        for i in range(len(s)):
            if listS[i] in listT:
                listT.remove(listS[i])
            else:
                return False

        return True