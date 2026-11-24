class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        unlocks = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            unlocks[prereq].append(course)
            indegrees[course] += 1

        queue = deque(i for i in range(numCourses) if indegrees[i] == 0)
        result = []
        while queue:
            pre = queue.popleft()
            result.append(pre)
            for course in unlocks[pre]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
            
        return result if len(result) == numCourses else []
                    

        