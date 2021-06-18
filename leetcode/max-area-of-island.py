class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if (len(grid)==0): return 0
        max_area = 0
        
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if (grid[i][j]==1):
                    count = self.backtrack(grid,i,j, row, col)
                    max_area = max(max_area,count)
        return max_area
    
    #backtrack
    def backtrack(self, grid: List[List[int]],x:int, y:int, row: int, col: int )->int:
        queue = []
        count = 1
        queue.append((x,y))
        #check the visited tile to zero so we dont have to visit it again
        grid[x][y] = 0
        
        while (len(queue) != 0):
            (x,y) = queue.pop(0)
            
            adj = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]

            for pos in adj:
                if (pos[0] >= 0) and (pos[0] < row) and (pos[1]>=0) and (pos[1]<col) and (grid[pos[0]][pos[1]]==1):
                    queue.append(pos)
                    grid[pos[0]][pos[1]]=0
                    count+=1
        return count
                    
