class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        up=0
        bottom=n-1
        row=0
        while up<=bottom:
            mid=(up+bottom+1)//2
            print(mid,matrix[mid][0])
            
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                if mid==n-1:
                    print("mid",mid)
                    row=n-1
                    break
                elif mid<n-1 and matrix[mid+1][0]>target:
                    print("row",mid)
                    row=mid
                    break
                else:
                    up=mid+1
            elif matrix[mid][0]>target:
                if mid>0 and matrix[mid-1][0]<target:
                    print("row1",mid)
                    row=mid-1
                    break
                else:
                    bottom=mid-1
        left=0
        right=m-1
        print(row)
        while left<=right:
            mid=(left+right+1)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False

        