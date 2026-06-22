# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        visited = set()
        while pointer is not None:
            if pointer in visited:
                return True
            
            visited.add(pointer)
            pointer = pointer.next
        
        return False