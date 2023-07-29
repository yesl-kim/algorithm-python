from collections import deque

class Node:
    def __init__(self,data) -> None:
        # data: {key:string, value:}
        self.data=data
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=None
        self.tail=None
        

    def get(self, key: int) -> int:
        node=self.cache.get(key)
        if not node:
            return -1
        # move to back
        self.delete(node)
        self.append(node)
        return node.data[1]
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache)==self.capacity:
            # popleft
            del self.cache[self.head.data[0]]
            head=self.head.next
            head.prev=None
            self.head=head
        node=Node((key,value))
        self.cache[key]=node
        self.append(node)


    def append(self,node):
        if not self.tail:
            node.next=None
            node.prev=None
            self.head=node
            self.tail=node
        else:
            node.next=None
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
    

    def delete(self,node):
        if node.prev:
            node.prev.next=node.next
        if node.next:
            node.next.prev=node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lru=LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))
lru.put(3,3)
print(lru.cache)
print(lru.get(2))
lru.put(4,4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))

# node=Node((1,10))
# print(node.data[1])