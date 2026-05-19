# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        visited = set([head])

        curr = head.next
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False
            

        