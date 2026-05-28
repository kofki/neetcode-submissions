class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.matrix = [[0 for _ in range(m)]for _ in range(n)]
        for i in range(n):
            s = 0
            for j in range(m):
                s += matrix[i][j]
                self.matrix[i][j] = s
        for i in range(m):
            s = 0
            for j in range(n):
                s += self.matrix[j][i]
                self.matrix[j][i] = s



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        diff = 0
        if row1 != 0:
            diff += self.matrix[row1-1][col2]
        if col1 != 0:
            diff += self.matrix[row2][col1-1]
        if col1 != 0 and row1 != 0:
            diff -= self.matrix[row1-1][col1-1]
        return self.matrix[row2][col2]-diff

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)