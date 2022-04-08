class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        returned = ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                returned = "".join(palindrome)
                break
            elif i == (len(palindrome) // 2 - 1):
                palindrome[-1] = "b"
                returned = "".join(palindrome)
            
        return returned
        
        
        
        
        
        
        
        
        
        
        
        
        
        # absmin = "".join(['z']*len(palindrome))
        # for i in range(len(palindrome)):
        #     for j in range(97,123):
        #         if j == ord(palindrome[i]):
        #             continue
        #         var = list(palindrome)
        #         var[i] = chr(j)
        #         if var != var[::-1]:
        #             absmin = min(absmin, "".join(var))
        # return absmin
            