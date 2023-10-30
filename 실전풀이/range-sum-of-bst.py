# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, node: Optional[TreeNode], low: int, high: int) -> int:
        if not node:
            return 0
        
        val = node.val if low <= node.val <= high else 0
        return val + self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)