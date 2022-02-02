class Solution:
    def minOperations(self, logs: List[str]) -> int:
        myStack=[]
        for i in logs:
            if i=="../":
                if len(myStack)>0:
                    myStack.pop()
            elif i[-2]!=".":
                myStack.append(i[:-1])
        return len(myStack)
            
        