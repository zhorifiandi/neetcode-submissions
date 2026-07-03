# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        pointer = head
        while pointer is not None:
            length += 1
            pointer = pointer.next
        

        if n == length:
            return head.next
        
        
        target = length - n
        i = 0
        pointer = head
        while pointer is not None:
            if i + 1 == target:
                targetNode = pointer.next
                pointer.next = targetNode.next
                break

            i += 1
            pointer = pointer.next
        
        return head