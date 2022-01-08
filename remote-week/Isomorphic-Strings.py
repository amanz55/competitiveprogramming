class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapDict={}
        mapped=[]
        for i in range(len(s)):
            if s[i] not in mapDict and t[i] in mapped:
                return False
            elif s[i] in mapDict:
                if mapDict[s[i]]!=t[i]:
                    return False
            elif s[i] not in mapDict and t[i] not in mapped:
                mapDict[s[i]]=t[i]
                mapped.append(t[i])
        return True
                
            
        
