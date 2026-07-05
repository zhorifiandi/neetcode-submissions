"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNewMapper = {None: None}
        
        dummy = Node(-1)
        new = dummy
        old = head

        while old:
            new.next = Node(old.val)
            oldToNewMapper[old] = new.next
            new = new.next
            old = old.next
        
        old = head
        new = dummy.next
        
        while new:
            new.random = oldToNewMapper[old.random]
            old = old.next
            new = new.next
           
        return dummy.next