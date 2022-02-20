class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        if len(tokens) == 1:
            return tokens[0]
        for i in tokens:
            if i == '+':
                a = myStack.pop()
                b = myStack.pop()
                myStack.append(int(a) + int(b))
            elif i == '-':
                a = myStack.pop()
                b = myStack.pop()
                myStack.append(int(b) - int(a))
            elif i == '*':
                a = myStack.pop()
                b = myStack.pop()
                myStack.append(int(a) * int(b))
            elif i == '/':
                a = myStack.pop()
                b = myStack.pop()
                myStack.append(int(b) / int(a))
            else:
                myStack.append(i)
                
        return int(myStack[0])
        