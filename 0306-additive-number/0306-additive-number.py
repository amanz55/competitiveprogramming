class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def valid(string):
            if len(string) == 1:
                return True
            if string[0] == "0":
                return False
            return True
            
        
        def backtrack(list_, idx, num):
            if idx >= len(num) and len(list_) >= 3:
                return True
            
            for i in range(idx, len(num)):
                val = num[idx : i + 1]
                if valid(val) and (len(list_) < 2 or (int(val) == int(list_[-1]) + int(list_[-2]))):
                    if backtrack(list_ + [val], i + 1, num):
                        return True
            return False
        
        return backtrack([], 0, num)