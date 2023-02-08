class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)
        
        for src, dest in adjacentPairs:
            pairs[src].append(dest)
            pairs[dest].append(src)
        start = -inf 
        for key in pairs:
            if len(pairs[key]) == 1:
                start = key
                break
                
        answer = [start]
        visited = set()
        visited.add(start)
        for _ in range(len(pairs)):
            for dest in pairs[answer[-1]]:
                if dest not in visited:
                    visited.add(dest)
                    answer.append(dest)
                
        return answer