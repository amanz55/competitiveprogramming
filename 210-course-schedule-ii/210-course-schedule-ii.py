class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        neighbours = defaultdict(set)
        
        for des, src in prerequisites:
            indegree[des] += 1
            neighbours[src].add(des)
            
        myque = deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                myque.append(i)
        
        new_arr = []
        
        while myque:
            temp = myque.popleft()
            new_arr.append(temp)
            for neighbour in neighbours[temp]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    myque.append(neighbour)
        return new_arr if len(new_arr) == numCourses else []