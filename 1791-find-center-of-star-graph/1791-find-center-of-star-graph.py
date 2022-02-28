class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result1 = edges[0][0]
        result2 = edges[0][1]
    
        if result1 in edges[1]:
            return result1
        elif result2 in edges[1]:
            return result2
            
        