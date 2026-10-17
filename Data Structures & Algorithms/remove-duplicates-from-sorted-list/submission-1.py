# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        # This is not a two pointer solution: only one pointer: current. 
        # For this solution: only move the pointer when you find a new unique value. 
        # if the next value is the same we keep moving hte next attribute of the current pointer, but the pointer stays at the same node. 

# This whole algorithm is go throught each node, and skip the node(cut of the node) that is similar, if different value in the next node we move to the next node. 

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
