class Solution:   
    def expressiveWords(self, s: str, words: List[str]) -> int:
        check = []
        last = s[0]
        count = 1
        for ch in s[1:]:
            if ch != last:
                check.append((last, count))
                last = ch
                count = 1
                
            else:
                count += 1
                
        check.append((last, count))
        answer = 0
        for word in words:
            l = 0
            last = word[0]
            count = 1
            for ch in word[1:]: 
                if l == len(check):
                    l = -1
                    break
                
                if ch != last:
                    temp = check[l][1]
                    if last == check[l][0] and (temp == count or (temp > 2 and count <= temp)):
                        l += 1
                        
                    last = ch
                    count = 1
                
                else:
                    count += 1
            
            if l == len(check):
                l = -1
                break
                
            if last == check[l][0] and (check[l][1] == count or (check[l][1] > 2 and count <= check[l][1])):
                l += 1   
            
            if l == len(check):
                answer += 1
        return answer