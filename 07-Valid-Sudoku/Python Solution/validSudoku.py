from collections import defaultdict

# Board will only ever be of size 9x9, if 
class Solution:
    def validSudoku(self, board):
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r // 3, c // 3) 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                #  If any element matches in the same row, column, or 3x3 square, return False
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        # If all checks out, return True
        return True
