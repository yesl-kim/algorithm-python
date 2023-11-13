from typing import List, Optional
from collections import defaultdict, deque
from itertools import zip_longest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        def recur(node):
            if not node:
                return
            yield [node.val]
            left = self.levelOrder(node.left)
            right = self.levelOrder(node.right)
            yield from (l + r for l, r in zip_longest(left, right, fillvalue=[]))
        return list(recur(node))


# root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print('=>',Solution().levelOrder(root))