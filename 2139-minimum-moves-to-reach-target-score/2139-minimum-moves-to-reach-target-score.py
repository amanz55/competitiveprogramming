class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1:
            if maxDoubles:
                if target % 2 == 0:
                    target /= 2
                    maxDoubles -= 1
                else:
                    target -= 1
            else:
                count += target - 1
                break
            count += 1
        return int(count)
        