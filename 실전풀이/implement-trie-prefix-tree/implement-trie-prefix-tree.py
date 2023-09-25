# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

     def __init__(self):
         self.words = set()

     def insert(self, word: str) -> None:
         self.words.add(word)

     def search(self, word: str) -> bool:
         return word in self.words


     def startsWith(self, prefix: str) -> bool:
         for word in self.words:
             if word.startswith(prefix):
                 return True
         return False