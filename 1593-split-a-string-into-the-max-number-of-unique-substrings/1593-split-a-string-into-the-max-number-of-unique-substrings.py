class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        answer = [0]
        
        def backtrack(list_, s, idx):
            if idx >= len(s):
                if len(list_) == len(set(list_)):
                    answer[0] = max(answer[0], len(list_))
                return
            
            for i in range(idx, len(s)):
                val = s[idx : i + 1]
                backtrack(list_ + [val], s, i + 1)
            
        backtrack([], s, 0)
        
        return answer[0]