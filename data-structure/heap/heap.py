class BinaryHeap:
    def __init__(self) -> None:
        self.items = [None]
    

    def __len__(self) -> None:
        return len(self.items) - 1
    

    def _percolate_up(self, child):
        parent = child // 2
        if not parent or self.items[parent] < self.items[child]:
            return
        
        self.items[child], self.items[parent] = self.items[parent], self.items[child]
        self._percolate_up(child // 2)

    
    def push(self, value) -> None:
        self.items.append(value)
        self._percolate_up(len(self))
        print(self.items)

bh = BinaryHeap()
bh.push(5)
bh.push(2)
bh.push(7)