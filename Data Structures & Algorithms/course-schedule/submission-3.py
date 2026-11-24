class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        unlocks = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            unlocks[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        taken = 0

        while queue:
            pre = queue.popleft()
            taken += 1
            for course in unlocks[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            
        return taken == numCourses