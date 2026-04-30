class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(st)==0:
                st.append(i)
            elif temperatures[st[-1]] >= temperatures[i]:
                st.append(i)
            else:
                while len(st)>0  and temperatures[st[-1]] < temperatures[i]:
                    last=st[-1]
                    cur=i
                    diff=cur-last
                    result[last]=diff
                    st.pop()
                st.append(i)
        return result
                
        