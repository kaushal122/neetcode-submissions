class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1=""
        for ch in s:
            if ch.isalnum():
                s1= s1+ch.lower()

       # print(s1)
        ptr1=0
        ptr2=len(s1)-1
        while(ptr1<=ptr2):
            if s1[ptr1]!=s1[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True
        