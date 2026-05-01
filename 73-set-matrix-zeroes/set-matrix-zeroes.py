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
        """

        #optimized
        m = len(matrix)
        n = len(matrix[0])
        firstrowzero = False
        firstcolzero = False

        #check first row
        for  j in range(n):
            if matrix[0][j] ==0:
                firstrowzero = True
        for i in range(m):
            if matrix[i][0] == 0:
                firstcolzero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j] ==0:
                    matrix[i][j] =0

        if firstrowzero:
            for j in range(n):
                matrix[0][j] = 0

        if firstcolzero:
            for i in range(m):
                matrix[i][0] = 0

