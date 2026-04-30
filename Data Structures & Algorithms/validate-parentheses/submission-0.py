class Solution:
    def isValid(self, s: str) -> bool:
        brcks={"]":"[", "}":"{",")":"("}
        st=[]
        for i in s:
            if brcks.get(i) and st and st[-1]==brcks[i]:
                st.pop()
            else:
                st.append(i)
        if len(st)>0:
            return False
        else:
            return True
                

