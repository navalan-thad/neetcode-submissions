class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            ind = self.keys.index(key)
            self.values[ind] = value
        else:
            self.keys.append(key)
            self.values.append(value)
        
    def get(self, key: int) -> int:
        if key in self.keys:
            return self.values[self.keys.index(key)]
        return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            ind = self.keys.index(key)
            self.keys.remove(key)
            self.values.remove(self.values[ind])
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)