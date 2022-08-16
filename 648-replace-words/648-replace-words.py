class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False



class Solution:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.isWord = True
        

    def search(self, word: str, isPrefix = False) -> bool:
        curr = self.root
        res = []
        for i in word:
            if i not in curr.children:
                return word
            res.append(i)
            curr = curr.children[i]
            if curr.isWord:
                break
        return "".join(res)
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        
        for j in dictionary:
            self.insert(j)
        for i in sentence.split(" "):
            result.append(self.search(i))
        return " ".join(result)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        