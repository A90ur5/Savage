# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastPointer, slowPointer = head, head
        
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True

        return False


'''
class Solution:
    def step(self, curNode):
        if curNode:
            return curNode.next
        else:
            return None


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slowPointer = head
        fastPointer = head.next
        while True:
            slowPointer = self.step(slowPointer)
            fastPointer = self.step(fastPointer)
            fastPointer = self.step(fastPointer)
            if not fastPointer:
                return False
            elif fastPointer == slowPointer:
                return True
'''         