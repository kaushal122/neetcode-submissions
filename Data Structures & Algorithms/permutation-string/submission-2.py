class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        arr=[0]*26

        for i in range(n):
            arr[ord(s1[i])-97] +=1
        p1=0
        p2=n-1
        n2=len(s2)
        if(n>n2):
            return False
        
        while p2<n2:
            temp=arr[:]
            #print(temp)
            for i in range(p1,p2+1):
                if temp[ord(s2[i])-97]==0:
                    p1+=1
                    p2+=1
                    continue
                else:
                    temp[ord(s2[i])-97] -= 1
                    if i==p2:
                        return True
            
        
        return False

