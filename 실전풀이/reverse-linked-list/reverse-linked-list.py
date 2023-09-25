# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        def recur(node):
            nonlocal new_head
            if not node.next:
                new_head = ListNode(node.val)
                return new_head
            
            next, cur = recur(node.next), ListNode(node.val)
            next.next = cur
            return cur
        
        recur(head)
        return new_head

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ans = s.reverseList(head)
while ans:
    print(ans.val)
    ans=ans.next