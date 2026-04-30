class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di=defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in di:
                temp = di[target-nums[i]]
                if temp<i:
                    return [temp,i]
                else:
                    return [i,temp]
            else:
                di[nums[i]] = i;
        return []