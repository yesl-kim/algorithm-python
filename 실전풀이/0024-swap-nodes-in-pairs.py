class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head 
        
        next = head.next
        next_next = head.next.next

        head.next, next.next = next_next, head
        head.next = self.swapPairs(next_next)
        return next