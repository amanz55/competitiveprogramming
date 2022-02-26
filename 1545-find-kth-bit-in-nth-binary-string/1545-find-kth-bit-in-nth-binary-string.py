class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(inverted) -> str:
            if inverted == "0":
                return "1"
            else:
                return "0"
            
        def recurse(n: int) -> str:
            if n == 1:
                return "0"
            else:
                before = recurse(n - 1)
                now = before + "1" + "".join(reversed(list(map(invert, list(before)))))
                return now
            
        answer = recurse(n)
        
        return answer[k-1]
            
            
        