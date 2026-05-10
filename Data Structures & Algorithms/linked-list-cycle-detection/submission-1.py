# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1=head

        if p1 is None or p1.next is None or p1.next.next is None:
            return False
        else:
            p2=p1.next.next
            while p1 is not None and p2 is not None:
                if p1==p2:
                    return True
                if p2.next is None:
                    return False
                p1=p1.next
                p2=p2.next.next
        return False
        
        