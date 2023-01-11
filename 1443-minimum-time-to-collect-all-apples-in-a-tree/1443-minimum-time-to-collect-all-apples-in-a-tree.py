class Solution:
    def dfs(self, node, adjlist, visited, hasApple):
        if not adjlist[node]:
            return hasApple[node] * 2
        
        visited.add(node)
        summ = 0
        for neighbour in adjlist[node]:
            if neighbour not in visited:
                summ += self.dfs(neighbour, adjlist, visited, hasApple)
        
        if summ == 0:
            return hasApple[node] * 2
        else:
            return summ + 2
        
        
        
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjlist = defaultdict(list)
        
        for source, dest in edges:
            adjlist[source].append(dest)
            adjlist[dest].append(source)
        
        visited = set()
        ans = self.dfs(0, adjlist, visited, hasApple)
        return max(0, ans - 2)