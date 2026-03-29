# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_list = []

        val = head
        while val != None:
            val_list.append(val)
            val = val.next

        new_list = []
        for i in range(1, len(val_list)+1):
            new_list.append(val_list[-i])

        for i in range(0, len(new_list)):
            if i<len(new_list)-1:
                new_list[i].next = new_list[i+1]
            else:
                new_list[i].next = None
        
        return new_list[0] if new_list else None          

