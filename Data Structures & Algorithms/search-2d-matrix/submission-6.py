class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if target > matrix[i][n-1]:
                continue
            elif target == matrix[i][n-1]:
                return True
            else: 
                s = 0
                e = n-1
                while s<=e:
                    mid = s + (e-s+1)//2
                    print(mid)
                    if target == matrix[i][mid]:
                        return True

                    elif target > matrix[i][mid]:
                        s = mid + 1
                    
                    else:
                        e = mid - 1
                return False
        return False