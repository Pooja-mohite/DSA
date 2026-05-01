class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #brute force
        """
        m = len(matrix)
        n = len(matrix[0])
        k = 1
        i = 0
        j = 0
        result = []
        while k <= (m+1)//2 and k <= (n+1)//2:
            while i < n-k and j == k-1:
                result.append(matrix[j][i])
                i = i+1
            while j< m-k and i == n-k:
                result.append(matrix[j][i])
                j = j + 1
            while i > k-1 and j == m-k:
                result.append(matrix[j][i])
                i = i-1
            while j > k-1 and i == k-1:
                result.append(matrix[j][i])
                j = j-1
            k = k+1
        if m == n and m % 2 != 0:
            mid = m // 2
            result.append(matrix[mid][mid])
        
        if m <n:
            row = m // 2
            for col in range(1, n-1):
                result.append(matrix[row][col])

        return result
        """
        #optimized
        result = []
        top = 0
        bottom= len(matrix) - 1
        left = 0
        right = len(matrix[0]) -1

        while top <= bottom and left <= right:
            for j in range(left, right +1):
                result.append(matrix[top][j])
            top = top +1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right = right- 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom = bottom - 1
            
            if left <= right:
                for i in range(bottom, top -1, -1):
                    result.append(matrix[i][left])
                left = left + 1
            
        return result

            

        