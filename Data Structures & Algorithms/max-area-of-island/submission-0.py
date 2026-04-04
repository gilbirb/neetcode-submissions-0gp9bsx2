class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        r, c = len(grid), len(grid[0])
        def dfs(x, y, prev_value):
            if x < 0 or y < 0 or x >= r or y >= c:
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x + 1, y, grid[x][y]) + dfs(x - 1, y, grid[x][y]) + dfs(x, y + 1, grid[x][y]) + dfs(x, y - 1, grid[x][y])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j, grid[i][j]), ans)

        return ans
