class TimeMap:

    def __init__(self):
        self.dic={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key]=[]
        self.dic[key].append((timestamp,value))
        #print(self.dic)

    def get(self, key: str, timestamp: int) -> str:
        st=""
        if key in self.dic:
            temp=self.dic[key]
            #print(temp)
            left=0
            right=len(temp)-1
            while left<=right:
                mid=(left+right)//2
                if temp[mid][0]<=timestamp:
                    st=temp[mid][1]
                    left=mid+1
                else:
                    right=mid-1
        return st

        
