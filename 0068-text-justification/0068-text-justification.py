class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        num_words = len(words)
        container = []
        ans = []
        
        i = 0
        while i < num_words:
            j = i
            spaces = 0
            temp = []
            summ = 0
            
            while j < num_words and summ + len(words[j]) + spaces <= maxWidth:
                summ += (len(words[j])  + spaces)
                temp.append(words[j])
                spaces = 1
                j += 1
            
            container.append(temp)
            i = j
        
        for i in range(len(container) - 1):
            cnt = len(''.join(container[i]))
            num_slots = max(len(container[i]) - 1, 1)
            temp = maxWidth - cnt
            s = temp // num_slots
            t = temp % num_slots
                
            lst = [container[i][0]]
            for j in range(1, len(container[i]) - 1):
                x = 0
                if t > 0:
                    x = 1
                    t -= 1
                    
                lst.append(' ' * (s + x))
                lst.append(container[i][j])
            
            lst.append(' ' * s)
            if len(container[i]) > 1:
                lst.append(container[i][-1])
            ans.append(''.join(lst))
        
        cnt = len(''.join(container[-1]))
        num_slots = len(container[-1]) - 1
        temp = maxWidth - cnt - num_slots
        ans.append(' '.join(container[-1]) + (' '* temp))
        return ans