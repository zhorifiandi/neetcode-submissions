# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return slow
    
    def reverse(self, head):
        prev = None
        p = head
        while p:
            pNext = p.next
            p.next = prev
            prev = p
            p = pNext
        
        return prev
    
    def alternatingMerge(self, l1, l2):
        p1 = l1
        p2 = l2
        while p1 and p2:
            p1Next = p1.next
            p2Next = p2.next
            p1.next = p2
            p2.next = p1Next
            p1 = p1Next
            p2 = p2Next
        

        self.print(l1)

        return l1
    
    def print(self, head):
        s = ""
        p = head
        while p:
            s += str(p.val)
            p = p.next
        
        print(s)
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        middleNode = self.findMiddle(head)
        tail = self.reverse(middleNode.next)
        middleNode.next = None
        head = self.alternatingMerge(head, tail)