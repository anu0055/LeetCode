class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        N = 9
        rows = [[0]*(N+1) for _ in range(N)]
        cols = [[0]*(N+1) for _ in range(N)]
        boxes = [[0]*(N+1) for _ in range(N)]
        isSolved = False

        def couldBePlaced(num, row, col):
            idx = (row//3)*3 + col//3
            return rows[row][num] + cols[col][num] + boxes[idx][num] == 0 #This means return true only if num is not in the row, col or that box (sum of all will be 0)
        
        def placeNumber(num, row, col):
            idx = (row//3)*3 + col//3
            rows[row][num] += 1
            cols[col][num] += 1
            boxes[idx][num] += 1
            board[row][col] = str(num)

        def removeNumber(num, row, col):
            idx = (row//3)*3 + col//3
            rows[row][num] -= 1
            cols[col][num] -= 1
            boxes[idx][num] -= 1
            board[row][col] = '.'

        def placeNextNumber(row, col):
            nonlocal isSolved
            if row == N-1 and col == N-1:
                isSolved = True
            elif col == N-1:
                backtrack(row+1, 0)
            else:
                backtrack(row, col+1)
        
        def backtrack(row, col):
            nonlocal isSolved
            if board[row][col] == '.':
                for num in range(1, 10):
                    if couldBePlaced(num, row, col):
                        placeNumber(num, row, col)
                        placeNextNumber(row, col)
                        if not isSolved:
                            removeNumber(num, row, col)
            else:
                placeNextNumber(row, col)

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)
        backtrack(0, 0)