# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helperfunction(self, head, n):
        if not head.next:
            return 1, None
        else:
            nodeNth, next2 = self.helperfunction(head.next, n)
            nodeNth += 1
            if nodeNth == n+1:
                head.next = next2
            return nodeNth, head.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        len ,_ = self.helperfunction(head, n)

        if len == n:
            return head.next
        else:
            return head