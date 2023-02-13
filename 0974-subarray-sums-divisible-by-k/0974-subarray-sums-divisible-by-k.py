class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running = 0
        count = 0
        remainder = defaultdict(int)
        remainder[0] = 1
        for num in nums:
            running += num
            modulo = running % k
            count += remainder[modulo]
            remainder[modulo] += 1
            
        return count