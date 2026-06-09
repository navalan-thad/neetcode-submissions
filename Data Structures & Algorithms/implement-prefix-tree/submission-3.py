class PrefixTree:

    def __init__(self):
        self.tree = {}
        
    def insert(self, word: str) -> None:
        curr = self.tree
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr['end'] = True
        
    def search(self, word: str) -> bool:

        curr = self.tree
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False

        if 'end' in curr and curr['end'] == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:

        curr = self.tree
        for char in prefix:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return True
        

        