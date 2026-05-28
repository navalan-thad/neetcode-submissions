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

        clones = {}
        curr = head
        while curr:
            new = Node(curr.val)
            clones[curr] = new
            curr = curr.next

        curr = head
        while curr:
            clone = clones[curr]
            clone.next = clones.get(curr.next)
            clone.random = clones.get(curr.random)
            curr = curr.next

        return clones[head]




        