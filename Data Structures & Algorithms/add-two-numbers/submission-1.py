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
        res=None
        prev=None
        
        while p1 or p2:
            t1=t2=0
            #print(p1.val,p2.val)
            if p1:
                #print(p1.val)
                t1=p1.val
                p1=p1.next
            if p2:
                print
                t2=p2.val
                p2=p2.next
            temp=t1+t2+carry
            if temp>9:
                carry=1
                temp=temp-10
            else:
                carry=0
            p=ListNode(temp)
            p.next=None
            if prev is not None:
                prev.next=p
                prev=p
            else:
                prev=p
                res=p
            
        if carry:
            p=ListNode(carry)
            p.next=None
            prev.next=p


        return res

        