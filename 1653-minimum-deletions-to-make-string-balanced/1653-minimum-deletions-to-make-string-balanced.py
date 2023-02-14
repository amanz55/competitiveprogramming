class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefix = [0]
        suffix = [0]
        length = len(s)
        answer = length
        
        for i in range(length):
            prefix.append(prefix[-1] + (s[i] == "b"))
            suffix.append(suffix[-1] + (s[length - i - 1] == "a"))
            
        suffix = suffix[::-1]
        
        for i in range(length):
            b = prefix[i]
            a = suffix[i+1]
            
            answer = min(answer, a + b)
            
        return answer