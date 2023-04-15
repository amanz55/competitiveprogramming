class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        answer = 0
        visited = set()
        
        def check(a, b, c, d, r):
            distance = ((c - a)**2 + (d - b)**2)**(0.5)
            return r >= distance
        
        def dfs(index):
            i, j, r = bombs[index]
            visited.add(index)
            
            for k in range(len(bombs)):
                a, b, c = bombs[k]
                if k not in visited and check(i, j, a, b, r):
                    dfs(k)
        
        for i in range(len(bombs)):
            dfs(i)
            answer = max(answer, len(visited))
            visited = set()
            
        return answer
                    