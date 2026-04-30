class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        print(s)
        lgst=0
        result=0
        for i, item in enumerate(s):
            if i==0:
                lgst += 1
                last =item
            elif item-last==1:
                lgst += 1
                last =item
            else:
                if lgst>result:
                    result=lgst
                lgst=1
                last=item
        if lgst>result:
            result=lgst

        return result

        