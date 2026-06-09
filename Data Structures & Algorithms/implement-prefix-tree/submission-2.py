class PrefixTree:

    def __init__(self):
        self.tree = {}
        
    def insert(self, word: str) -> None:
        
        pointer = self.tree
        for char in word:
            if char not in pointer:
                pointer[char] = {}
            pointer = pointer[char]
        pointer['*'] = True

    def search(self, word: str) -> bool:

        curr = self.tree
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False

        if '*' in curr and curr['*'] == True:
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
        
        