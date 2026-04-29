class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            box = set()
            row = set()
            col = set()
            for j in range(9):
                r = board[i][j]
                if r != ".":
                    if r in row:
                        print(f"row: {i}, {j}")
                        return False
                    else:
                        row.add(r)
                c = board[j][i]
                if c != ".":
                    if c in col:
                        print(f"col: {i}, {j}")
                        return False
                    else:
                        col.add(c)
                b = board[(i//3)*3 + j // 3][(i % 3)*3 + j % 3]
                if b != ".":
                    if b in box:
                        print(f"box: {i}, {j}, {b}")
                        return False
                    else:
                        box.add(b)

        return True