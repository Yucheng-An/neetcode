class Solution:
    def searchMatrix(self, matrix, target):
        up = 0
        down = len(matrix) - 1
        targetRow = 0
        while up <= down:
            row = (up + down) // 2
            if target < matrix[row][0]:
                down = row - 1
            elif target > matrix[row][-1]:
                up = row + 1
            else:
                targetRow = row
                break
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[targetRow][mid]:
                right = mid - 1
            elif target > matrix[targetRow][mid]:
                left = mid + 1
            else:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 11
obj = Solution()
print(obj.searchMatrix(matrix, target))
