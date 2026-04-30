class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        un={}
        res=0
        p1=0
        for i in range(len(s)):
            print(un)
            print("cha",s[i])
            print("p1",p1)
            # case when char is present in string
            if s[i] in un and un[s[i]]>=p1:
                temp=i-p1
                print("temp",temp)
                res=max(res,temp)
                p1=un[s[i]]+1
                print("updated",p1)
                un[s[i]]=i
                
            else:
                un[s[i]]=i
        n=len(s)       
        res=max(res,n-p1)
        return res


