class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        colors = [WHITE] * numCourses
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course:int) -> bool:
            colors[course] = GRAY
            for prereq in graph[course]:
                if colors[prereq] == GRAY:
                    return True
                if colors[prereq] == WHITE:
                    if dfs(prereq):
                        return True
                if colors[prereq] == BLACK:
                    continue
            colors[course] = BLACK
            return False
        
        for course in range(numCourses):
            if colors[course] == WHITE:
                if dfs(course):
                    return False
        return True