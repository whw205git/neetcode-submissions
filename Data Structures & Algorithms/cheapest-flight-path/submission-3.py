class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        
        cheapest = {src: 0}
        queue = deque([(0, src)])
        
        steps = 0
        while queue and steps <= k:
            for _ in range(len(queue)):
                cost, stop = queue.popleft()

                for next, next_cost in graph[stop]:
                    cost_to_next = cost + next_cost
                    if next not in cheapest or cheapest[next] > cost_to_next:
                        queue.append((cost_to_next, next))
                        cheapest[next] = cost_to_next
            steps += 1
        
        return -1 if dst not in cheapest else cheapest[dst]