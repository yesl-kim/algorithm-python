# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        cur = head
        
        while cur:
            print(f"{prev.val if prev else prev} -> {cur.val} -> {cur.next.val if cur.next else cur.next}")
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        
        return prev

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.reverseList(head))