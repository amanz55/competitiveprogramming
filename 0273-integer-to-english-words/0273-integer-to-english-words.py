class Solution:
    def __init__(self):
        self.dictionary = {'1': "One",'2': "Two",'3': "Three",'4': "Four",'5': "Five",'6': "Six",'7': "Seven",'8': "Eight",'9': "Nine",'10': "Ten",'11': "Eleven",'12': "Twelve",'13': "Thirteen",'14': "Fourteen",'15': "Fifteen",'16': "Sixteen",'17': "Seventeen",'18': "Eighteen",'19': "Nineteen",'20': "Twenty",'30': "Thirty",'40': "Forty",'50': "Fifty",'60': "Sixty",'70': "Seventy",'80': "Eighty",'90': "Ninety"}
        
    def findWord(self, num):
        result = deque()
        
        if int(num[-1]) > 0:
            result.appendleft(self.dictionary[num[-1]])
        
        if len(num) > 1:
            if num[-2] == '1':
                if result:
                    result.pop()
                result.appendleft(self.dictionary[num[-2:]])
            elif int(num[-2]) > 1:
                result.appendleft(self.dictionary[num[-2] + '0'])
                
        if len(num) > 2 and num[-3] != '0':
            result.appendleft("Hundred")
            result.appendleft(self.dictionary[num[-3]])
        
        result.reverse()
        return list(result)
        
    def numberToWords(self, nums: int) -> str:
        if nums == 0:
            return 'Zero'
        string = str(nums)
        length = len(string)
        count = 0
        answer = []
        
        while string:
            hund = self.findWord(string[-3:])
            
            if count == 1 and hund:
                answer.append("Thousand")
            
            elif count == 2 and hund:
                answer.append("Million")
                
            elif count == 3 and hund:
                answer.append("Billion")
                
            answer.extend(hund)
            string = string[:-3]
            count += 1
            
        answer = answer[::-1]
        return ' '.join(answer)