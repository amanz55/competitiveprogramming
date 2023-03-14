class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answer = []
        
        def backtrack(list_, idx, s, wordDict):
            if idx >= len(s):
                answer.append(" ".join(list_))
                return
            
            for i in range(idx, len(s)):
                val = s[idx : i + 1]
                if val in wordDict:
                    backtrack(list_ + [val], i + 1, s, wordDict)
                    
        backtrack([], 0, s, wordDict)
        return answer