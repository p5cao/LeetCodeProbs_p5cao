class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        count = 0
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        from collections import deque

        def bfs(row:int, col:int) -> bool:
            if grid[row][col] == "0":
                return False
            queue = deque([(row,col)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    r_nb, c_nb = r+dr, c+dc
                    if 0<=r_nb<=nrow-1 and 0<=c_nb<=ncol-1 and grid[r_nb][c_nb] == "1":
                        grid[r_nb][c_nb] = "0"
                        queue.append((r_nb, c_nb))
            return True
        
        for r in range(nrow):
            for c in range(ncol):
                if bfs(r, c):
                    count += 1
        return count

