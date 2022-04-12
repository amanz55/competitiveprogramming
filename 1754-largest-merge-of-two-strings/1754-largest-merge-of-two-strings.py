class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # word = "hello"
        # print(max(word[:2], word[2:])[0])
        index1 = index2 = 0
        merge = []
        while True:
            if index1 < len(word1) and index2 < len(word2):
                if word1[index1] > word2[index2]:
                    merge.append(word1[index1])
                    index1 += 1
                elif word1[index1] < word2[index2]:
                    merge.append(word2[index2])
                    index2 += 1
                else:
                    if word1[index1:] > word2[index2:]:
                        merge.append(word1[index1])
                        index1 += 1
                    else:
                        merge.append(word2[index2])
                        index2 += 1
            elif index1 < len(word1):
                merge.append(word1[index1:])
                break
            elif index2 < len(word2):
                merge.append(word2[index2:])
                break
        return "".join(merge)
            
                
        