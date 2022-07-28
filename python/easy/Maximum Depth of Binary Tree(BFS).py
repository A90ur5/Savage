# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        bfsQue = deque([root])
        level = 0
        while bfsQue:
            level += 1
            for i in range(len(bfsQue)):
                node = bfsQue.popleft()
                if node.left:
                    bfsQue.append(node.left)
                if node.right:
                    bfsQue.append(node.right)
        return level