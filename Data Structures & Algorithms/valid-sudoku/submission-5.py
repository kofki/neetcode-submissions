class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        box = set()
        for i in range(9):
            for j in range(9):
                r = board[i][j]
                c = board[j][i]
                b = board[(i // 3) * 3 + (j // 3)][(i % 3) * 3 + (j % 3)]

                if r in row or c in col or b in box:
                    return False
                else:
                    row.add(r) if r != "." else ...
                    col.add(c) if c != "." else ...
                    box.add(b) if b != "." else ...
            row.clear()
            col.clear()
            box.clear()
        return True