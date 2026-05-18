
class Solution(object):
    def orangesRotting(self, grid):
        '''
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        while True:
            newRotten = []
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        if i+1 < rows and grid[i+1][j] == 1:
                            newRotten.append((i+1,j))
                        if i-1 >= 0 and grid[i-1][j]== 1:
                            newRotten.append((i-1, j))
                        if j+1 < cols and grid[i][j+1] == 1:
                            newRotten.append((i, j+1))
                        if j-1 >= 0 and grid[i][j-1] == 1:
                            newRotten.append((i, j-1))
            if len(newRotten) == 0:
                break
            for x,y in newRotten:
                grid[x][y] = 2
            minutes = minutes + 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return minutes
        '''
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh = fresh + 1
        minutes = 0
        while queue and fresh>0:
            size = len(queue)
            for k in range(size):
                i,j = queue.popleft()
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j]=2
                    queue.append((i-1,j))
                    fresh = fresh - 1
                if i+1 < rows and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1,j))
                    fresh = fresh -1 
                if j-1 >= 0 and grid[i][j-1]==1:
                    grid[i][j-1] = 2
                    queue.append((i,j-1))
                    fresh = fresh - 1
                if j+1 < cols and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i, j+1))
                    fresh = fresh -1
            minutes = minutes+1
        if fresh == 0:
            return minutes
        return -1










            
















                    


       
        