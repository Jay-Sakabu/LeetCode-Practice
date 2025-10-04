from collections import defaultdict

# Board will only ever be of size 9x9, if 
class Solution:
    def validSudoku(self, board):
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r // 3, c // 3) represents 3x3 sub-grid

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                #  If any element matches in the same row, column, or 3x3 sub-grid, return False
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        # If all checks pass, return True
        return True
