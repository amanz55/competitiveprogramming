
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        mydict = {}
        
        for k in range(1,len(isConnected) + 1):
            mydict[k] = []
            for j in isConnected[k - 1]:
                mydict[k].append(j)
        
                
                
        def dfs(val):
            for i in range(len(mydict[val])):
                if mydict[val][i] == 1 and i + 1 not in visited:
                    visited.add(i + 1)
                    dfs(i + 1)
                
        for key in mydict:
            if key not in visited:
                provinces += 1
                dfs(key)
                
        return provinces
                