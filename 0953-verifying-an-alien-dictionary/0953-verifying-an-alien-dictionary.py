class Solution:
    def __init__(self):
        self.dictionary = {}
    
    def sorting(self, x, y):
        length = min(len(x), len(y))
            
        for i in range(length):
            if self.dictionary[x[i]] > self.dictionary[y[i]]:
                return 1
            
            elif self.dictionary[x[i]] < self.dictionary[y[i]]:
                return -1
            
        return 1 if len(x) > len(y) else -1
        
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, char in enumerate(order):
            self.dictionary[char] = i+1
            
        words2 = sorted(words, key = functools.cmp_to_key(self.sorting))
        
        return words == words2