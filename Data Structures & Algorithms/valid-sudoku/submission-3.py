class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for num in range(1,10):
                row.add(str(num))
                col.add(str(num))
                box.add(str(num))
            for j in range(9):
                if board[i][j] in row: 
                    row.remove(board[i][j])
                elif board[i][j] != ".": return False
                if board[j][i] in col: col.remove(board[j][i])
                elif board[j][i] != ".": return False
                cell = board[(i//3)*3+j//3][(i%3)*3+j%3]
                if cell in box: box.remove(cell)
                elif cell != ".": return False
        return True 