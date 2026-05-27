class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity

        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        temp = node.prev
        temp.next = node.next
        node.next.prev = temp

    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = temp

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert(self.cache[key])
            return

        node = Node(key, value)

        if len(self.cache) >= self.size:
            keyToDelete = self.left.next
            del self.cache[keyToDelete.key]
            self.remove(keyToDelete)
        
        self.insert(node)
        self.cache[node.key] = node

        
