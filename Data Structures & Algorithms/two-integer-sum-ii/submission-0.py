class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for idx1 in range(n):
            for idx2 in range(idx1+1,n):
                if numbers[idx1]+numbers[idx2]== target:
                    return [idx1+1,idx2+1]
        return [-1,-1]
        