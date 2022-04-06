class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        end = len(people) - 1
        start = 0
        count = 0
        people.sort()
        
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            count += 1
            end -= 1

        return count
        