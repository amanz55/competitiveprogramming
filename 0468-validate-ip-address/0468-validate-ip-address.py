class Solution:
    def check_v4(self, string):
        temp = string.split(".")
        if len(temp) != 4:
            return False
        for num in temp:
            if len(num) == 0:
                return False
            if len(num) > 1 and num[0] == "0":
                return False
            if num.isdigit():
                if int(num) > 255 or int(num) < 0:
                    return False
            for ch in num:
                if ord(ch) > 57 or ord(ch) < 48:
                    return False
                
        return True
        
    def check_v6(self, string):
        temp = string.split(":")
        if len(temp) != 8:
            return False
        for num in temp:
            if len(num) > 4 or len(num) <= 0:
                return False
            for ch in num:
                if 65 <= ord(ch) <= 70 or 97 <= ord(ch) <= 102 or 48 <= ord(ch) <= 57:
                    continue
                else:
                    return False
                
        return True
        
        
        
        
    def validIPAddress(self, queryIP: str) -> str:
        answer = queryIP.split(".")
        result = "Neither"
        if len(answer) == 1:
            if self.check_v6(queryIP):
                result = "IPv6"
        else:
            if self.check_v4(queryIP):
                result = "IPv4"
            
        return result