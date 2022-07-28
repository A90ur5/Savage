# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    hashmap = set()

    def dfs_MerkleTree_noHashMap(self, root):
        if root.left:
            leftHash = self.dfs_MerkleTree(root.left)
        else:
            leftHash = 'NULL'
        if root.right:
            rightHash = self.dfs_MerkleTree(root.right)
        else:
            rightHash = 'NULL'
        return str(hash(leftHash + rightHash + str(root.val)))

    def dfs_MerkleTree(self, root):
        if root.left:
            leftHash = self.dfs_MerkleTree(root.left)
        else:
            leftHash = 'NULL'
        if root.right:
            rightHash = self.dfs_MerkleTree(root.right)
        else:
            rightHash = 'NULL'
        curHash = str(hash(leftHash + rightHash + str(root.val)))
        self.hashmap.add(curHash)
        return curHash

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.hashmap.clear()
        self.dfs_MerkleTree(root)
        subTreeHash = self.dfs_MerkleTree_noHashMap(subRoot)
        if subTreeHash in self.hashmap:
            return True
        else:
            return False
        
        
