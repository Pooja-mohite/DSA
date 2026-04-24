class Solution(object):
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        directions = []
        directions.append((1,0))
        directions.append((-1,0))
        directions.append((0,1))
        directions.append((0,-1))

        def dfs(r, c, visited, ocean):
            #check if reached ocean
            if ocean == "pacific":
                if r == 0 or c == 0:
                    return True

            if ocean == "atlantic":
                if r == rows - 1 or c == cols - 1:
                    return True

            #mark visited
            visited.add((r,c))

            #explore all directions
            for i in range(len(directions)):

                dr = directions[i][0]
                dc = directions[i][1]

                nr = r + dr
                nc = c + dc

                #check boundary
                if nr >= 0  and nr < rows and nc >= 0 and nc < cols:
                    #check water flow condition
                    if heights[nr][nc] <= heights[r][c]:

                        #check visited
                        if (nr, nc) not in visited:
                            #recursive call
                            result = dfs(nr, nc, visited, ocean)
                            if result == True:
                                return True
            
           #if no path found
            return False
    
       # final result list
        answer = []

        for i in range(rows):
            for j in range(cols):

                #create new visisted set for pacific
                visited1 = set()

                #check pacific
                canReachPacific = dfs(i, j, visited1, "pacific")

                #create new visited set for atlantic
                visited2 = set()

                #check atlantic
                canReachAtlantic = dfs(i, j, visited2, "atlantic")

                #if both true
                if canReachPacific == True and canReachAtlantic == True:
                    answer.append([i, j])

        return answer




        
        