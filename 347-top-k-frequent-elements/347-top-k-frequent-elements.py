from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = Counter(nums)
        myheap = []
        for key, value in mydict.items():
            if len(myheap) < k:
                heappush(myheap, (value, key))
            else:
                if value > myheap[0][0]:
                    heappop(myheap)
                    heappush(myheap, (value, key))
                    
        return list( map(itemgetter(1), myheap ))
        