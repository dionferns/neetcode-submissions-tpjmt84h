# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        org_value = head


        if not head: 
            return head

        i = org_value
        j = org_value.next

        while j: 
            if i.val != j.val: 
                i.next = j
                i = i.next
            j = j.next
        
        i.next = None
        return org_value
