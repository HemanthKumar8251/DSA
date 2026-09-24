class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for course,preq in prerequisites:
            adj[preq].append(course)
            indegree[course]+=1
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        count = 0
        while q:
            curr = q.popleft()
            for i in adj[curr]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            count +=1
        return count==numCourses