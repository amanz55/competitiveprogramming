class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
            
        visit = [0] * n
        visited = set()
        
        def dfs(node, past):
            nonlocal visit
            visit[node - 1] = past
            visited.add(node)
            for nei in graph[node]:
                if visit[nei - 1] != 0 and visit[nei - 1] == past:
                    return False
                if nei not in visited and not dfs(nei, -past):
                    return False
            return True
        
        for node in range(1, n + 1):
            if not visit[node - 1]:
                if not dfs(node, 1):
                    return False
        return True