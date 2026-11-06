# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        # mark position n elements before the end and have node before = node after (effectively removing it)

        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        # fast now points to nth node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # fast will end at last node, slow will be right before node to remove
        slow.next = slow.next.next
        return dummy.next

        
        