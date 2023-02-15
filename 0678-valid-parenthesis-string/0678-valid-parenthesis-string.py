class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        memo = {}
        
        def checker(idx, stack):
            if idx >= len(s):
                if not stack:
                    return True
                else:
                    return False
            if (idx, tuple(stack)) in memo:
                return memo[(idx, tuple(stack))]
            
            if s[idx] == "(":
                stack.append("(")
                return checker(idx + 1, stack)
            elif s[idx] == ")":
                if stack:
                    stack.pop()
                    return checker(idx + 1, stack)
            else:
                one = checker(idx + 1, stack.copy())
                two = checker(idx + 1, stack + ["("])
                three = checker(idx + 1, stack.copy()[:-1])
                
                memo[(idx, tuple(stack))] = one or two or three
                return one or two or three
            
        return checker(0, stack)