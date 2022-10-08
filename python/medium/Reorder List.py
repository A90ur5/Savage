#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp_array = []
        cur_node = head
        while cur_node:
            tmp_array.append(cur_node)
            cur_node = cur_node.next
        
        cur_node = head
        n = len(tmp_array)
        even = True if n%2 == 0 else False
        for i in range(1, n//2+1):
            cur_node.next = tmp_array[n-i]
            #if even and i == n//2:
            if even and i == n>>1:
                cur_node = cur_node.next
            else:
                cur_node.next.next = tmp_array[i]
                cur_node = tmp_array[i]
        cur_node.next = None