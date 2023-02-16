class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        string = list(s)
        memo = {}
        
        def helper(idx, left, last, count):
            if left < 0:
                return float('inf')
            
            if idx == len(s):
                return 0
            
            if (idx, left, last, count) in memo:
                return memo[(idx, left, last, count)]
                
            answer = 0
            if s[idx] == last:
                inc = 0
                if count == 1 or count == 9 or count == 99:
                    inc = 1
                    
                answer = inc + helper(idx + 1, left, last, count + 1)
                    
            else:
                pick = 1 + helper(idx + 1, left, s[idx], 1)
                
                jump = helper(idx + 1, left - 1, last, count)
                
                answer = min(pick, jump)
            
            memo[(idx, left, last, count)] = answer
            return answer
            
        return helper(0, k, '', 0)