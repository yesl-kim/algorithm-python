# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class NotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Trie:
    def __init__(self):
        self.root = Node()


    def find(self, s: str) -> Node:
        node = self.root
        for char in s:
            if not char in node.next:
                raise NotFoundError(node, char)
            node = node.next[char]
        return node
    

    def insert(self, word: str) -> None:
        while True:
            try:
                self.find(word).isEnd = True
                return
            except NotFoundError as error:
                node, char = error.args
                node.next[char] = Node()

        
    def search(self, word: str) -> bool:
        try:
            return self.find(word).isEnd
        except NotFoundError:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        try:
            self.find(prefix)
            return True
        except NotFoundError:
            return False
        

t = Trie()
t.insert('apple')
print(t.search('app'))
print(t.search('apple'))
print(t.startsWith('app'))