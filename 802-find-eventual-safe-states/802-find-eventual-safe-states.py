class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graphq = defaultdict(set)
        outdegree = defaultdict(int)
        terminals = []
        ans = []
        for i in range(len(graph)):
            if graph[i] == []:
                terminals.append(i)
                ans.append(i)
                continue
            
            for k in range(len(graph[i])):
                graphq[graph[i][k]].add(i)
                outdegree[i] += 1
            
        queue = deque(terminals)
            
        while queue:
            curr = queue.popleft()
            for key in graphq[curr]:
                    outdegree[key] -= 1
                    if outdegree[key] == 0:
                        queue.append(key)
                        ans.append(key)
        return sorted(ans)