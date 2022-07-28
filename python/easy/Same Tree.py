# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def DFS(root):
            if root.left != None:
                LVal = DFS(root.left)
            else:
                LVal = 'N'

            if root.right != None:
                RVal = DFS(root.right)
            else:
                RVal = 'N'
            
            return [root.val, LVal, RVal]
        if p != None:
            pList = DFS(p)
        else:
            pList = None

        if q != None:
            qList = DFS(q)
        else:
            qList = None

        if pList == qList:
            return True
        else:
            return False
