class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            t1=target-numbers[i]
            t2=self.search(numbers, t1,i+1)
            if t2!=-1:
                return [i+1,t2+1]
        
        return [-1,-1]

    
    def search(self, numbers: List[int], t1:int, idx:int) -> int:
        n=len(numbers)
        i=idx
        l=n-1
        while i<=l:
            mid= (l+i) // 2
            if numbers[mid]==t1:
                return mid
            elif numbers[mid]<t1:
                i=mid+1
            elif numbers[mid]>t1:
                l=mid-1
        return -1
                

