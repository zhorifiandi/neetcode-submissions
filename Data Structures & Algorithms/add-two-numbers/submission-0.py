# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointerToNewHead = ListNode(-1)
        p1, p2 = l1, l2
        newPointer = pointerToNewHead
        carryOver = 0
        
        while p1 or p2:
            newValue = carryOver
            if p1:
                newValue += p1.val
            if p2:
                newValue += p2.val

            remainder = newValue % 10
            carryOver = newValue // 10
            
            newPointer.next = ListNode(remainder)
            
            newPointer = newPointer.next

            if p1:
                p1 = p1.next
            
            if p2:
                p2 = p2.next
        

        if carryOver > 0:
            newPointer.next = ListNode(carryOver)
        

        return pointerToNewHead.next