# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        nodeDict = {}
        curNode = head
        while curNode:
            if curNode in nodeDict:
                return True
            else:
                nodeDict[curNode] = True
                curNode = curNode.next
        return False