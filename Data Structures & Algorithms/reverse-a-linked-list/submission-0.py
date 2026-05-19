# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        curr = head.next
        prev = head
        prev.next = None

        while curr:
            temp = curr.next # 2
            curr.next = prev # 1-->0
            prev = curr
            curr = temp # curr: 2

        return prev

        