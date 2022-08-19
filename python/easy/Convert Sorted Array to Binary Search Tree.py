# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binarySearch(l ,r):
            m = (l + r) // 2
            if r < l:
                return None
            '''
            if r == l:
                return TreeNode(nums[m], None, None)
            elif r - l < 2:
                return TreeNode(nums[m], None, TreeNode(nums[r], None, None))
            '''
            return TreeNode(nums[m], binarySearch(l, m-1), binarySearch(m+1, r))

        l, r = 0, len(nums)-1
        m = (l + r) // 2
        return TreeNode(nums[m], binarySearch(l, m - 1), binarySearch(m + 1, r))
