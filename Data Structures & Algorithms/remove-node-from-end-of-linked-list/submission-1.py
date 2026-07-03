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
        

        dummy = ListNode(-1, head)
        
        target = length - n
        
        i = 0
        prev = dummy
        pointer = head
        while pointer is not None:
            if i == target:
                prev.next = pointer.next
                break

            i += 1
            prev = pointer
            pointer = pointer.next
        
        return dummy.next