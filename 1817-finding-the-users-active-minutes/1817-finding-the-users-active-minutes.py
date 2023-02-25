class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        id_min = defaultdict(set)
        
        for iD, mint in logs:
            id_min[iD].add(mint)
            
        answer = [0] * k
        
        for key in id_min:
            answer[len(id_min[key]) - 1] += 1
            
        return answer
            