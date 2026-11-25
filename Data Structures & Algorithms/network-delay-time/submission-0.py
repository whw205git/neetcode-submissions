class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create a graph of node ID to all reachable nodes and times
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        shortest = {}
        min_heap = [(0, k)]

        while min_heap:
            elapsed, node = heapq.heappop(min_heap)
            if node in shortest:
                continue

            shortest[node] = elapsed

            for neighbor in graph[node]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, (elapsed + neighbor[1], neighbor[0]))

        if len(shortest) != n:
            return -1

        return max(shortest.values())
