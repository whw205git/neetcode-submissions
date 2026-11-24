class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        s1_count = Counter(s1)
        window_count = Counter()
        window_size = len(s1)

        for i, c in enumerate(s2):
            window_count[c] += 1
            if i >= window_size:
                left_char = s2[i-window_size]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1
            if window_count == s1_count:
                return True

        return False 