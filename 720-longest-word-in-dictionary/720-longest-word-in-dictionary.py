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
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if not curr.children[i].isWord:
                return False
            curr = curr.children[i]
        return True
        
    def longestWord(self, words: List[str]) -> str:
        for i in words:
            self.insert(i)
        ans = ""
        for i in words:
            if self.search(i):
                if len(ans) < len(i):
                    ans = i
                elif len(ans) == len(i):
                    ans = min(ans, i)
        return ans
        
        


        
        