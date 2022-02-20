class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]   
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[" :
                stack.append(s[i])
            elif len(stack)==0:
                return False
            elif  stack[-1]=="(" and s[i]==")":
                stack.pop()
            elif  stack[-1]=="{" and s[i]=="}":
                stack.pop()
            elif  stack[-1]=="[" and s[i]=="]":
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
                
            
        