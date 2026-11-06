class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        from collections import deque
        nrow, ncol = len(image), len(image[0])
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        orig_color = image[sr][sc]

        if orig_color == color:
            return image

        def bfs(row:int, col:int) -> None:
            # color the starting pixel
            image[row][col] = color
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<=nrow-1 and 0<=nc<=ncol-1:
                        if image[nr][nc] == orig_color:
                            image[nr][nc] = color
                            queue.append((nr, nc))
            # return True
        
        bfs(sr, sc)
        return image
