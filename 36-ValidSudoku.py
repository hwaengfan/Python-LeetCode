def isValidSudoku(board):
    def checkRow(board, row):
        seen = set()
        for i in range(9):
            if board[row][i] != '.':
                if board[row][i] in seen:
                    return False
            else:
                seen.add(board[row][i])
        return True

    def checkCol(board, col):
        seen = set()
        for i in range(9):
            if board[i][col] != '.':
                if board[i][col] in seen:
                    return False
            else:
                seen.add(board[i][col])
        return True

    def checkGrid(board, xPos, yPos):
        seen = set()
        gridX = xPos - xPos % 3
        gridY = yPos - yPos % 3

        for i in range(3):
            for j in range(3):
                curr = board[gridX + i][gridY + j]
                if curr != '.':
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)
        return True

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            else:
                if not (checkRow(board, i) and checkCol(board, j) and checkGrid(board, i, j)):
                    return False
    return True
