"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        curr = head
        copies = {}

        while curr:
            newNode = Node(curr.val)
            copies[curr] = newNode
            curr = curr.next

        curr = head

        while curr:
            clone = copies[curr]
            clone.next = copies.get(curr.next)
            clone.random = copies.get(curr.random)
            curr = curr.next

        return copies[head]



        



        