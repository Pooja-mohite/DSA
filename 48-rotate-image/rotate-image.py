class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Brute Force:
        n = len(matrix)
        result = []
        
        #create new matrix
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            result.append(row)
        # fill new matrix
        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = matrix[i][j]

        #copy back to original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j]= result[i][j]

        

        