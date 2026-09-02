# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        leftPrev = dummy
        curr = head

        for _ in range(left-1):
            leftPrev = curr
            curr = curr.next
        sublist_tail = curr # will be tail of reversed section

        prev = None
        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is at posn right, curr is at right+1
        sublist_tail.next = curr # connect reversed tail to right
        leftPrev.next = prev # connect left to reversed head
        
        return dummy.next

        
        