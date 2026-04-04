class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y, componentOf, compNo):
            if x < 0 or y < 0 or x >= rows or y >= cols:
                return
            if componentOf[x][y] != "-1" or grid[x][y] == "0":
                return
            
            componentOf[x][y] = compNo
            dfs(x + 1, y, componentOf, compNo)
            dfs(x - 1, y, componentOf, compNo)
            dfs(x, y + 1, componentOf, compNo)
            dfs(x, y - 1, componentOf, compNo)


        componentOf = [["-1" for _ in range(cols)] for _ in range(rows)]
        compNo = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                v = grid[i][j]
                if v == "0":
                    continue
                else:
                    if componentOf[i][j] == "-1":
                        dfs(i, j, componentOf, compNo)
                        compNo += 1

        return compNo