# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1=l1
        p2=l2
        carry=0
        dummy=ListNode()
        curr=dummy


        
        while p1 or p2 or carry:
            t1=t2=0
            if p1:
                t1=p1.val
                p1=p1.next
            if p2:
                t2=p2.val
                p2=p2.next
            temp=t1+t2+carry
            if temp>9:
                carry=1
                temp=temp-10
            else:
                carry=0
            curr.next=ListNode(temp)
            curr=curr.next

        return dummy.next

        