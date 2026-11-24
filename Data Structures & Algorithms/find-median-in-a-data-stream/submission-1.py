class MedianFinder:

    def __init__(self):
        self.low = [] # max heap storing smaller numbers
        self.high = [] # min heap storing larger numbers

    def addNum(self, num: int) -> None:

        # push into low, pop low, and push into high
        tmp = -heapq.heappushpop(self.low, -num)
        heapq.heappush(self.high, tmp)
            
        # Always keep low to be same size or +1 than high. 
        # If imbalanced, pop from high and insert into low
        if len(self.high) > len(self.low):
            tmp = heapq.heappop(self.high)
            heapq.heappush(self.low, -tmp)        

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        return -self.low[0]
        
        