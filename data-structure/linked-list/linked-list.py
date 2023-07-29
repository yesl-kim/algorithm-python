class ListNode:
    def __init__(self, value):
        self.value=value
        self.next=None

# def printNode(node):
#     print(node.value)
#     if node.next:
#         printNode(node.next)

def printNode(node):
    cur=node
    while cur:
        print(cur.value)
        cur=cur.next

class SLinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def addAtHead(self,value):
        node=ListNode(value)
        node.next=self.head
        self.head=node
    
    def addAtBack(self,value):
        cur=self.head
        while cur.next:
            cur=cur.next
        node=ListNode(value)
        cur.next=node

    def find(self,value):
        node=self.head
        while node:
            if node.value==value:
                return node
            node=node.next
        raise RuntimeError('node not found')

    def addAfter(self,node,value):
        new=ListNode(value)
        node.next,new.next=new,node.next
            

# list node
# head=ListNode(1)
# head.next=ListNode(2)
# head.next.next=ListNode(3)
# printNode(head)

# singled linked list
print('-'*10)
s_linked_list=SLinkedList()
s_linked_list.addAtHead(1)
s_linked_list.addAtHead(2)
s_linked_list.addAtBack(3)
s_linked_list.addAfter(s_linked_list.find(1),4)
printNode(s_linked_list.head)