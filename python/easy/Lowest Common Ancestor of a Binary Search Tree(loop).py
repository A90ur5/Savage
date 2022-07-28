# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        minnum = min(p.val, q.val)
        maxnum = max(p.val, q.val)
        while cur:
            if (maxnum >= cur.val) and (minnum <= cur.val):
                return cur
            elif minnum > cur.val:
                cur = cur.right
            else:
                cur = cur.left
