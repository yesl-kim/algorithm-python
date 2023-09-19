# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, cur):
            if not cur:
                return prev
            next, cur.next = cur.next, prev
            return reverse(cur, next)
        
        return reverse(None, head)

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ans = s.reverseList(head)
while ans:
    print(ans.val)
    ans=ans.next