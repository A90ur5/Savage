# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        elif(list2 == None):
            return list1
        
        if(list1.val < list2.val):
            myList = list1
            myHead = myList
            if(list1.next != None):
                list1 = list1.next
            else:
                myList.next = list2
                return myHead
        else:
            myList = list2
            myHead = myList
            if(list2.next != None):
                list2 = list2.next
            else:
                myList.next = list1
                return myHead
                
        while(True):
            if(list1.val < list2.val):
                myList.next = list1
                myList = myList.next
                if(list1.next != None):
                    list1 = list1.next
                else:
                    myList.next = list2
                    break
            else:
                myList.next = list2
                myList = myList.next
                if(list2.next != None):
                    list2 = list2.next
                else:
                    myList.next = list1
                    break

        return myHead