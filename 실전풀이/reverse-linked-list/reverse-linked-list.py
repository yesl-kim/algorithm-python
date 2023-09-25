# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(node):
            if not node.next:
                new_head = ListNode(0, ListNode(node.val))
                return new_head.next, new_head
            
            next, head = recur(node.next)
            cur = ListNode(node.val)
            next.next = cur
            return cur, head
        
        _, new_head = recur(head)
        return new_head.next

s = Solution()
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode()
ans = s.reverseList(head)
while ans:
    print(ans.val)
    ans=ans.next