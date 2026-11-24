class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        dependencies = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            dependencies[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1
            for dep in dependencies[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
            
        return taken == numCourses