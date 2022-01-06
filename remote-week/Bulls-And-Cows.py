class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secrets=list(secret)
        guesses=list(guess)
        bulls=0
        cows=0
        for i in range(len(guesses)):
            if guesses[i]==secrets[i]:
                    bulls+=1
                    secrets[i]=" "
                    guesses[i]=" "           
        for j in range(len(guesses)):
            if secrets.count(guesses[j])>0 and guesses[j]!=" ":
                cows+=1
                for k in range(len(secrets)):
                    if secrets[k]==guesses[j]:
                        secrets[k]=" "
                        break
        return str(bulls)+'A'+str(cows)+'B'
        
