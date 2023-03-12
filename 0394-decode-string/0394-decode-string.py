class Solution:
    def decode(self, string, idx, prev_str, prev_num):
        if idx >= len(string):
            return prev_str, idx
        
        while idx < len(string):
            while string[idx].isdigit():
                prev_num = prev_num * 10 + int(string[idx])
                idx += 1
            if string[idx] == "[":
                ret_str, ret_pos = self.decode(string, idx + 1, "", 0)
                prev_str += ret_str * prev_num
                idx = ret_pos + 1
                prev_num = 0
            elif string[idx] == "]":
                return prev_str, idx
            else:
                prev_str += string[idx]
                prev_str, idx = self.decode(string, idx + 1, prev_str, prev_num)
                        
        return prev_str, idx + 1
        
        
        
    def decodeString(self, s: str) -> str:
        return self.decode(s, 0, "", 0)[0]
        