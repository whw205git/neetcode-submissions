class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        
        cheapest = {}
        queue = deque()
        queue.append((0, src))
        
        steps = 0
        while queue and steps <= k:
            for _ in range(len(queue)):
                cost, stop = queue.popleft()

                for neighbor in graph[stop]:
                    cost_to_neighbor = cost + neighbor[1]
                    if neighbor[0] not in cheapest or cheapest[neighbor[0]] > cost_to_neighbor:
                        queue.append((cost_to_neighbor, neighbor[0]))
                        cheapest[neighbor[0]] = cost_to_neighbor
            steps += 1
        
        return -1 if dst not in cheapest else cheapest[dst]