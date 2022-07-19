class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mydict = {}
        ans = []
        
        for i in range(n):
            mydict[i] = i
            
        for i in edges:
            mydict[i[1]] = mydict[i[0]]
            
        for items in mydict:
            if mydict[items] == items:
                ans.append(items)
        
        return ans
        
        