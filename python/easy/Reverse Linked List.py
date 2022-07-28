# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastNode = None
        curNode = head
        while curNode:
            temp = curNode.next
            curNode.next = lastNode
            lastNode = curNode
            curNode = temp
        return lastNode
        