# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1=head
        p2=head
# this part to divide the list into parts
        while p1 and p1.next:
            if p1.next.next is None:
                p1=p1.next
            else:
                p1=p1.next.next
            p2=p2.next
#reverse second part
        l1=head
        l2=p2.next
        p2.next=None
        cur=l2
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        l2=prev
# merge both the list
        p1=l1
        while l2:
            temp=l1.next
            temp2=l2.next
            l1.next=l2
            l2.next=temp
            l1=temp
            l2=temp2

        head=p1
     


            
        