class Solution:
    def reverseParentheses(self, s: str) -> str:
        myStack = []
        for i in s:
            if i != ")":
                myStack.append(i)
            else:
                var = []
                while True:
                    if myStack[-1] != "(":
                        var.append(myStack.pop())
                    else:
                        myStack.pop()
                        for i in var:
                            myStack.append(i)
                        break
        
        return "".join(myStack)
        