class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_number = defaultdict(list)
        
        for i in range(len(routes)):
            for stop in routes[i]:
                bus_number[stop].append(i)
        
        # stop_visited = set()
        queue = deque()
        
        # stop_visited.add(source)
        bus_visited = set()
        queue.append(source)
        level = 0
        
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                cur = queue.popleft()
                
                if cur == target:
                    return level
                
                for number in bus_number[cur]:
                    if number not in bus_visited:
                        for stop in routes[number]:
                            # if stop not in stop_visited:
                            queue.append(stop)
                                # stop_visited.add(stop)
                                
                    bus_visited.add(number)
            level += 1
        
        return -1
                    
        
            