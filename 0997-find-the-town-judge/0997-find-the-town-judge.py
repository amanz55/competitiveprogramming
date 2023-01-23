class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        visited = set()
        
        for src, dest in trust:
            trusts[dest] += 1
            visited.add(src)
            
        for i in range(1, n + 1):
            if i not in visited and trusts[i] == n - 1:
                return i
        return -1