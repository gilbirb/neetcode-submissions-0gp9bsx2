class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols:
                return
            if grid[x][y] == "0":
                return
            
            grid[x][y] = "0"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        compNo = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                v = grid[i][j]
                if v == "0":
                    continue
                else:
                    dfs(i, j)
                    compNo += 1

        return compNo