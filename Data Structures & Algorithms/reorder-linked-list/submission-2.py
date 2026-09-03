# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # sever connection
        curr = slow.next
        slow.next = None

        # reverse 2nd half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge halves
        first = head
        second = prev

        while second:
            # store nexts
            temp1 = first.next
            temp2 = second.next

            # wire to correct next step
            first.next = second
            second.next = temp1

            # take step forward
            first = temp1
            second = temp2
        
        
