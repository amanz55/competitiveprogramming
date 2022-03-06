class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mydict = Counter(words)
        myheap = []
        for key in mydict:
            heappush(myheap, (-1 * mydict[key], key))
        res = []
        for i in range(k):
            res.append(heappop(myheap)[1])
        return res 