# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        p2=head

        if not head or head.next== None:
            return head
        else:
            if head is not None:
                p1=head.next

            while p1 is not None:
                temp=p1.next
                p1.next=p2
                p2=p1
                p1=temp
            head.next=None
            head=p2
        
        return head


        