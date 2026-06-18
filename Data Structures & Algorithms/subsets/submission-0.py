class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def sets(index:int,current:List):
            res.append(current[:])

            for i in range(index,len(nums)):
                current.append(nums[i])
                sets(i+1,current)
                current.pop()
        
        sets(0,[])

        return res


        