from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        # 0 = unvisited, 1 = visiting, 2 = done
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:  # cycle detected
                return False
            if state[node] == 2:  # already verified safe
                return True

            state[node] = 1       # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2       # mark as done
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True