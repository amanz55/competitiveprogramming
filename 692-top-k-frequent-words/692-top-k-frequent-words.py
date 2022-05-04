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
            words.append([i,root.children[i].freq])
        words.sort(key=lambda x: x[1], reverse=True)
        result =[]
        res = []
        print(words)
        for i in range(len(words)):
            if len(res) == 0 or words[i][1] == res[-1][1]:
                res.append(words[i])
            else:
                result.extend(sorted(res))
                res = [words[i]]
        result.extend(sorted(res))
        for i in range(len(result)):
            result[i] = result[i][0]
        return result[:k]