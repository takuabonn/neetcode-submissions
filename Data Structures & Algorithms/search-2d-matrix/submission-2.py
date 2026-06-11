class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        rLeft, rRight = 0, len(matrix)-1
        print(rLeft, rRight)
        # 行を特定
        while rLeft < rRight:
            mid = rLeft + (rRight-rLeft)//2
           
            row = matrix[mid]
            if target >= row[0] and target <= row[rowLen-1]:
                print(mid,"jj")
                rLeft = mid
                break
            if target < row[0]:
                rRight = mid - 1
            if target > row[rowLen-1]:
                rLeft = mid + 1
        
        left, right = 0, rowLen-1
        print(rLeft)
        while left <= right:
            mid = left + (right-left)//2
            if target == matrix[rLeft][mid]:
                return True
            if target < matrix[rLeft][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
