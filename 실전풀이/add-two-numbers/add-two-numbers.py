# https://leetcode.com/problems/add-two-numbers
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def up(self, node: ListNode):
        if not node:
            return
        
        if node.val >= 10:
            next_val, node.val = divmod(node.val, 10)
            if node.next:
                node.next.val += next_val
            else:
                node.next = ListNode(next_val)
        self.up(node.next)
        
                
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode() # placeholder
        n1, n2 = l1, l2
        while n1 and n2:
            node.next = ListNode(n1.val + n2.val)
            node = node.next
            n1, n2 = n1.next, n2.next
        
        if n1:
            node.next = n1

        if n2:
            node.next = n2
        
        self.up(head.next)
        return head.next
    

s = Solution()
n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))
node = s.addTwoNumbers(n1, n2)
while node:
    print(node.val, end='')
    node = node.next