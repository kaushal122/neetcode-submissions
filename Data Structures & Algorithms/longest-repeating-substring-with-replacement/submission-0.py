class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr=[0]*26
        left=0
        right=0
        mch=0
        res=0
        for i in range(len(s)):
            temp=ord(s[i])-ord('A')
            lngth=right-left+1
            if i==0:
                arr[temp] = 1
                mch=1
                right += 1
            else:
                arr[temp] += 1
                if arr[temp]>mch:
                    mch=arr[temp]
                if lngth-mch<=k:
                    res=max(res,lngth)
                else:
                    arr[ord(s[left])-ord('A')] -=1
                    mch=max(arr)
                    left +=1
                right +=1
        return res

                



                


            


        