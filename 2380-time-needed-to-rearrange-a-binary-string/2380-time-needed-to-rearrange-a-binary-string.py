class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        answer = 0
        has = True
        
        while has:
            has = False
            new = s.copy()
            for i in range(1, len(s)):
                if s[i] == "1" and s[i - 1] == "0":
                    has = True
                    new[i], new[i - 1] = new[i - 1], new[i]
            s = new
            if has:
                answer += 1
        return answer
                    
                    
                    
        