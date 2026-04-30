class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
           # print(result)
            num1=nums[i]
            idx1=i+1
            idx2=n-1
            while idx1 <idx2:
                sum2 = nums[idx1]+nums[idx2]
                if  sum2+num1==0:
                    result.append([nums[i],nums[idx1],nums[idx2]])
                    idx1 += 1
                    idx2 -= 1
                    while idx1<idx2 and nums[idx1]==nums[idx1-1]:
                        idx1 += 1
                    while idx1<idx2 and nums[idx2] == nums[idx2+1]:
                        idx2 -= 1
                elif sum2+num1<0 :
                    idx1 += 1
                elif sum2+num1 >0 :
                    idx2 -= 1
        return result
        