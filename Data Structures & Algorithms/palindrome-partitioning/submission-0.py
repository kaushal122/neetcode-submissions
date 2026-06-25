class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        n=len(s)

        def backtrack(start:int,path:List[str]):
            if start==n:
                res.append(path[:])
            
            for end in range(start+1,n+1):
                subs=s[start:end]
                if subs==subs[::-1]:
                    path.append(subs)
                    backtrack(end,path)
                    path.pop()
        backtrack(0,[])
        return res

