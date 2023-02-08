class Solution:
    def dfs(self, graph, dividend, target, visited):
        if dividend == target:
            return 1
        
        visited.add(dividend)
        for div in graph[dividend]:
            if div[0] not in visited:
                var = self.dfs(graph, div[0], target, visited)
                if var != -1:
                    return var * div[1]
                
        return -1
            
            
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        equation_length = len(equations)
        
        for i in range(equation_length):
            pair = equations[i]
            graph[pair[0]].append((pair[1], values[i]))
            graph[pair[1]].append((pair[0], 1 / values[i]))
            
        answer = []
        
        for query in queries:
            if query[0] in graph:
                result = self.dfs(graph, query[0], query[1], set())
                answer.append(result)
            else:
                answer.append(-1)
            
        return answer
        