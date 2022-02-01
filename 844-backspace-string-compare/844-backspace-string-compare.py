class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS=[]
        stackT=[]
        ptr=0
        while ptr<len(s):
            if s[ptr]!='#':
                stackS.append(s[ptr])
            else:
                if len(stackS)!=0:
                    stackS.pop()
            ptr+=1
        ptr=0
        while ptr<len(t):
            if t[ptr]!='#':
                stackT.append(t[ptr])
            else:
                if len(stackT)!=0:
                    stackT.pop()
            ptr+=1
        if stackS==stackT:
            return True
        else:
            return False
        
                
        