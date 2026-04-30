class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped=list(zip(position,speed))
        zipped.sort(reverse=True)
       # print(zipped)
        st=[]
        res=0
        for i,pair in enumerate(zipped):
            time=(target-pair[0])/pair[1]
           # print("t",time)
            if i==0:
                st.append(time)
            elif time<=st[-1]:
                continue
            else:
                st.pop()
                st.append(time)
                res+=1
        if len(st)>0:
            res +=1
        return res
        