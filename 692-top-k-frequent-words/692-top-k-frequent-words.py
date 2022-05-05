class Node:
    def __init__(self):
        self.freq = 1
        self.children = {}



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        root = Node()
        for i in words:
            if i in root.children:
                root.children[i].freq += 1
            else:
                root.children[i] = Node()
        words = []
        for i in root.children:
            words.append([-1 * root.children[i].freq,i])
        words.sort()
        for i in range(len(words)):
            words[i] = words[i][1]
        return words[:k]