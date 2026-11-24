class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_locations = {}
        longest_len = 0
        start = 0

        for i, c in enumerate(s):
            if c in last_locations and last_locations[c] >= start:
                start = last_locations[c] + 1
            last_locations[c] = i
            longest_len = max(longest_len, i - start + 1)

        return longest_len