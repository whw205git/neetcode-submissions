class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp is strictly increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key)
        # do a modified binary search to find largest timestamp < timestamp
        if not values:
            return ""

        l = 0 
        r = len(values) - 1
        ans = None
        while (l <= r):
            m = (l+r) // 2
            if timestamp < values[m][0]:
                r = m - 1
            else:
                ans = m
                l = m + 1
        
        return "" if ans is None else values[ans][1]





        
