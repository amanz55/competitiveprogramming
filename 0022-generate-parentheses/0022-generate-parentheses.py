class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def dp(op_count, cl_count, path):
            if op_count == 0 and cl_count == 0:
                answer.append("".join(path))
                return
            
            if op_count > 0:
                path.append("(")
                dp(op_count - 1, cl_count, path)
                path.pop()
        
            if op_count < cl_count:
                path.append(")")
                dp(op_count, cl_count - 1, path)
                path.pop()
                
        dp(n, n, [])
        
        return answer