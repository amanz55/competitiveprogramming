class Solution:
    def compute(self, a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        return a * b

    @lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression:
            return []
        if expression.isdigit():
            return [int(expression)]
        
        ans = []
        for ind, i in enumerate(expression):
            if not i.isdigit():
                a = self.diffWaysToCompute(expression[:ind])
                b = self.diffWaysToCompute(expression[ind+1:])
                
                for x in a:
                    for y in b:
                        ans.append(self.compute(x, y, i))
            
        
        return ans
            