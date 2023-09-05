# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        node1, node2 = list1, list2
        
        while node1 and node2:
            print(f"cur: {cur.val}, ", end=' ')
            print(f"node1: {node1.val}, ", end=' ')
            print(f"node2: {node2.val}")
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        
        if node1:
            cur.next = node1
        
        if node2:
            cur.next = node2
        
        return head.next
    

s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
res = s.mergeTwoLists(list1, list2)
while res:
    print(res.val)
    res = res.next