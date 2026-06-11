class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        rLeft, rRight = 0, len(matrix) - 1

        # 行を特定
        while rLeft <= rRight:
            mid = rLeft + (rRight - rLeft) // 2
            row = matrix[mid]

            if target < row[0]:
                rRight = mid - 1
            elif target > row[rowLen - 1]:
                rLeft = mid + 1
            else:
                # 見つかった行
                left, right = 0, rowLen - 1
                while left <= right:
                    m = left + (right - left) // 2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        left = m + 1
                    else:
                        right = m - 1
                return False

        return False