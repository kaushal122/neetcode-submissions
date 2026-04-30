class MinStack:
  


    def __init__(self):
        self.arr=[]
        self.arr2=[]

    def push(self, val: int) -> None:
        self.arr.append(val)
        val=min(val,self.arr2[-1] if self.arr2 else val)
        self.arr2.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.arr2.pop()
        

    def top(self) -> int:
        return self.arr[-1]

        

    def getMin(self) -> int:
        return self.arr2[-1]
