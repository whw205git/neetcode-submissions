from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in counter.items():
            buckets[frequency].append(num)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

        # return [item[0] for item in counter.most_common(k)]
