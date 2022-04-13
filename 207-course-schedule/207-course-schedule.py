class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbours = defaultdict(set)
        
        for des, src in prerequisites:
            indegree[des] += 1
            neighbours[src].add(des)
            
        myque = deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                myque.append(i)
        
        length = 0
        
        while myque:
            temp = myque.popleft()
            length += 1
            for neighbour in neighbours[temp]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    myque.append(neighbour)
        return length == numCourses