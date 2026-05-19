# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        remove = stack[-n]

        if len(stack) == n:
            return head.next

        prev = stack[-n-1]

        prev.next = remove.next
        remove = None

        return head
        