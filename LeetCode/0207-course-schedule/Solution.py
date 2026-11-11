class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        # | Color | Value | Meaning |
        # | `WHITE` | `0` | DFS hasn’t visited this course yet. |
        # | `GRAY` | `1` | This course is on the current DFS recursion path. |
        # | `BLACK` | `2` | DFS has finished exploring this course and its outgoing edges without finding a cycle. |
        colors = [WHITE] * numCourses
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        def dfs(course:int)->bool: # return True if finds a cycle
            colors[course] = GRAY
            for neighbor in graph[course]:
                if colors[neighbor] == GRAY:
                    return True
                if colors[neighbor] == WHITE and dfs(neighbor):
                    return True
            colors[course] = BLACK
            return False
        
        for course in range(numCourses):
            if colors[course] == WHITE and dfs(course):
                return False
        return True