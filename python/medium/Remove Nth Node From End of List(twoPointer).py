# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        firstPointer = dummyNode
        secondPointer = dummyNode
        while n > 0 and secondPointer:
            secondPointer = secondPointer.next
            n -= 1

        while secondPointer.next:
            secondPointer = secondPointer.next
            firstPointer = firstPointer.next

        firstPointer.next = firstPointer.next.next

        return dummyNode.next

