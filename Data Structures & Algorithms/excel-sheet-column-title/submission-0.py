import string 

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        mapping = {}
        count = 1

        for letter in string.ascii_uppercase:
            mapping[count] = letter
            count += 1
        
        title = ""

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            title = mapping[remainder+1] + title
            columnNumber //= 26

        return title


        