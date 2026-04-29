class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n -1
        while l <= r:
            guess = l + (r-l) // 2 
            if matrix[guess // n][guess % n] > target:
                r = guess - 1
            elif matrix[guess // n][guess % n] < target:
                l = guess + 1
            else:
                return True
        return False