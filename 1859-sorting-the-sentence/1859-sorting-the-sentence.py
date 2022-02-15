class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        s.sort(key = lambda x:x[-1])
        s = list(map(list, s))
        for i in s:
            i.pop()
        s = list(map("".join, s))
        s = " ".join(s)
        
        return s
        