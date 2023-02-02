class Solution:
    def sorting(self, x, y):
        check_x = x[x.index(" ") + 1:]
        check_y = y[y.index(" ") + 1:]
        
        if check_x == check_y:
            check_x = x[:x.index(" ")]
            check_y = y[:y.index(" ")]
            
        return 1 if check_x > check_y else -1
        
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if 48 <= ord(log[-1]) <= 57:
                digits.append(log)
            else:
                letters.append(log)     
        letters = sorted(letters, key = functools.cmp_to_key(self.sorting))
        letters.extend(digits)
        
        return letters