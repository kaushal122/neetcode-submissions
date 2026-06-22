class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(idx,combo,current_sum):
            if current_sum==target:
                res.append(combo[:])
            elif current_sum>target:
                return 
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                combo.append(candidates[i])
                backtrack(i+1,combo,current_sum+candidates[i])
                combo.pop()

        backtrack(0,[],0)

        return res
