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
                
        answer = [start, pairs[start][0]]
        
        for _ in range(len(pairs) - 2):
            dest = pairs[answer[-1]]
            if dest[0] != answer[-2]:
                answer.append(dest[0])
            else:
                answer.append(dest[1])
                
        return answer