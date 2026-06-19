# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        top = head
        curr = head
        while curr.next:
            temp = curr.next
            node = ListNode(math.gcd(curr.val, temp.val))
            curr.next = node
            node.next = temp
            curr = temp

        return top
        