class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        available_tasks = [count for task, count in counter.items()]
        heapq.heapify_max(available_tasks)

        time = 0
        holdoff_queue = deque()
        while available_tasks or holdoff_queue:
            time += 1
            if not available_tasks:
                # if there are no tasks that we can start immediately, pull tasks from holdoff queue
                time = holdoff_queue[0][1]
            else:
                # if there are available tasks, start with the most frequent one
                count = heapq.heappop_max(available_tasks)
                count -= 1
                # put in the holdoff queue if there are tasks remaining
                if count > 0:
                    holdoff_queue.append((count, time + n))

            # if the first item in queue is processed, put it back in available tasks
            if holdoff_queue and holdoff_queue[0][1] == time:
                heapq.heappush_max(available_tasks, holdoff_queue.popleft()[0])

        return time

