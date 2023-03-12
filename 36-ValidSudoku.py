class Solution:
    def checkRow(self, board, row):
        seen = set()
        for i in range(9):
            if board[row][i] != '.':
                if board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        return True

    def checkCol(self, board, col):
        seen = set()
        for i in range(9):
            if board[i][col] != '.':
                if board[i][col] in seen:
                    return False
                else:
                    seen.add(board[i][col])
        return True

    def checkBox(self, board, row, col):
        seen = set()
        x = row - row % 3
        y = col - col % 3
        for i in range(3):
            for j in range(3):
                num = board[x + i][y + j]
                if num != '.':
                    if num in seen:
                        return False
                    else:
                        seen.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not (self.checkRow(board, i) and self.checkCol(board, j) and self.checkBox(board, i, j)):
                        return False
        return True
