class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        # brute force:
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        for (i,j) in zeros:
            for col in range(n):
                matrix[i][col] = 0
            for row in range(m):
                matrix[row][j] = 0
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [0] *m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(m):
            for j in range(n):
                if rows[i] == 1 or cols[j] ==1:
                    matrix[i][j] = 0

