# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1=head
        total=0
        prev=None

        while p1:
            total += 1
            p1=p1.next
        target=total-n+1
        #print(total,target)
        if total==1:
            head=None
            return head
        elif target==1:
            prev=head
            head=head.next
            prev.next=None
            return head
        
        p1=head
        prev=None
        #print(target)
        while target>1 and p1:
            prev=p1
            p1=p1.next
            target -=1
            #print(target)
        #print(p1.val,prev.val)
        prev.next=p1.next
        p1.next=None
        return head

        
