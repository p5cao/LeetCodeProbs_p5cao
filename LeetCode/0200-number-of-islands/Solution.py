class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        count = 0
        def dfs(col, row)->bool:
            if not (0<=col<=ncol-1 and 0<=row<=nrow-1):
                return False
            if grid[row][col] == "0":
                return False
            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(col-1, row)
                dfs(col+1, row)
                dfs(col, row-1)
                dfs(col, row+1)
                return True

        for ii in range(ncol):
            for jj in range(nrow):
                if dfs(ii,jj):
                    count += 1
        return count

