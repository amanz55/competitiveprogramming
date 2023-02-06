class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        answer = 1
        dictionary = defaultdict(int)
        
        for word in words:
            dictionary[word] = max(dictionary[word], 1)
            for idx in range(len(word)):
                sliced = word[:idx] + word[idx + 1:]
                if sliced in dictionary:
                    dictionary[word] = max(dictionary[sliced] + 1, dictionary[word])
                    answer = max(answer, dictionary[word])
            
        return answer
            