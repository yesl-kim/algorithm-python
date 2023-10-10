# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        if not node1 and not node2:
            return
        if (not node1 and node2) or (node1.val > node2.val):
            node1, node2 = node2, node1
            
        node1.next = self.mergeTwoLists(node1.next, node2)
        return node1
    

s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
res = s.mergeTwoLists(list1, list2)
while res:
    print(res.val)
    res = res.next