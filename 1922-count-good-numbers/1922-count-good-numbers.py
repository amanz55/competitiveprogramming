class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = 10**9 + 7
        
        if n % 2 == 0:
            result = pow(5,n//2,mod) * pow(4,n//2,mod)
        else:
            result = pow(5,(n+1)//2,mod) * pow(4,((n + 1)//2 - 1),mod)
        
        return result % mod
        