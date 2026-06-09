class PrefixTree:

    def __init__(self):
        self.tree = {}
        
    def insert(self, word: str) -> None:
        self.tree[word] = True

    def search(self, word: str) -> bool:
        if word in self.tree:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        for key in self.tree.keys():
            if len(prefix) <= len(key) and prefix == key[:len(prefix)]:
                return True
        return False
        
        