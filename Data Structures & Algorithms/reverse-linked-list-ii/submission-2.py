class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        node = ListNode(0)
        node.next = head
        curr = head
        beforeLeft = node

        for _ in range(left-1):
            beforeLeft = curr
            curr = curr.next

        tail = curr

        prev = None

        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        tail.next = curr
        beforeLeft.next = prev

        return node.next



        
        