class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # python has min heap, but i need to get rid of the largest distance, so need to negate the distance
        min_heap = []

        for point in points:
            distance = -1 * math.sqrt(point[0] ** 2 + point[1] ** 2)

            if len(min_heap) < k:
                heapq.heappush(min_heap, (distance, point))
            elif distance > min_heap[0][0]:
                heapq.heapreplace(min_heap, (distance, point))

        return [point for _, point in min_heap]