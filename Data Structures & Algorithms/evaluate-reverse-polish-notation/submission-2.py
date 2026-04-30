class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in range(len(tokens)):
            temp=tokens[i]
            if temp in ["+", "-", "*", "/"]:
                t1 = st[-1]
                print(t1)
                st.pop()
                t2 = st[-1]
                print(t2)
                st.pop()
                if temp=="/":
                    t=int(t2/t1)
                elif temp=="+":
                    t = t2+t1
                elif temp=="-":
                    t=t2-t1
                elif temp=="*":
                    t=t2*t1
                print(t,"t")
                st.append(t)     
            else:
                st.append(int(tokens[i]))
        
        return st[-1]