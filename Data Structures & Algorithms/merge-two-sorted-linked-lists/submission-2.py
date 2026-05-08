# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=list1
        cur2=list2
        prev1=None
        prev2=None
    
        while cur1 is not None and cur2 is not None:
            if cur1.val<=cur2.val:
                print(cur1.val,cur2.val)
                prev1=cur1
                cur1=cur1.next              
                if prev2 is None:
                    prev1.next=list2
                    list2=prev1
                    cur2=list2
                else:
                    prev1.next=cur2
                    prev2.next=prev1
                    prev2=prev1

                
                print(list2.next.val)
            else:
                while cur2 is not None and cur1.val>cur2.val:
                    print(cur1.val," * ",cur2.val)
                    prev2=cur2
                    cur2=cur2.next
        if cur1 is not None and prev2 is not None:
            prev2.next=cur1
        if list1 is not None and list2 is None:
            return list1
        else:
            return list2
        