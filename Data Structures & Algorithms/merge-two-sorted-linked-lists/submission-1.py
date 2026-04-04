# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(-1)

        pointer = newList
        p1 = list1
        p2 = list2

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                pointer.next = p1
                pointer = p1
                p1 = p1.next
            else:
                pointer.next = p2
                pointer = p2
                p2 = p2.next
        

        if p1 is not None:
            pointer.next = p1
        else:
            pointer.next = p2
        
        return newList.next
