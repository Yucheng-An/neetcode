"""
We can use set() in row, col, grid to check
"""
class Solution:
    def isValidSudoku(self, board):
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        grid = [[set() for _ in range(3)] for _ in range(3)]
        print(grid)
        print(3//3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet[r]:
                    return False
                if board[r][c] in colSet[c]:
                    return False
                if board[r][c] in grid[r//3][c//3]:
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                grid[r//3][c//3].add(board[r][c])
        return True



board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
       ["4", ".", ".", "5", ".", ".", ".", ".", "."],
       [".", "9", "8", ".", ".", ".", ".", ".", "3"],
       ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
       [".", ".", ".", "8", ".", "3", ".", ".", "5"],
       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
       [".", ".", ".", ".", ".", ".", "2", ".", "."],
       [".", ".", ".", "4", "1", "9", ".", ".", "8"],
       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

obj= Solution()
print(obj.isValidSudoku(board))




