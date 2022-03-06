class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mydict = Counter(words)
        myheap = []
        for key, value in mydict.items():
            heappush(myheap, (-1 * value, key))
        res = []
        for i in range(k):
            res.append(heappop(myheap)[1])
        return res        