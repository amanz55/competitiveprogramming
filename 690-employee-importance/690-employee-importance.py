"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mydict = {}
        visited = set()
        self.totalImportance = 0
        for i in employees:
            mydict[i.id] = [i.importance, i.subordinates]

        def dfs(rt):
            visited.add(rt)
            self.totalImportance += mydict[rt][0]
            for i in mydict[rt][1]:
                dfs(i)
            return
                    
        dfs(id)
        return self.totalImportance
        