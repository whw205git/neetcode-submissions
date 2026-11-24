class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window_count, t_count = Counter(), Counter(t)
        have, need = 0, len(t_count)
        left = 0
        shortest_string = ""

        for right in range(len(s)):
            rc = s[right]
            window_count[rc] += 1
            if rc in t_count and window_count[rc] == t_count[rc]:
                have += 1

            while have == need:
                # update minimum window result here
                if shortest_string == "" or len(shortest_string) >= right - left + 1:
                    shortest_string = s[left:right+1]

                # shrink left
                lc = s[left]
                window_count[lc] -= 1
                if lc in t_count and window_count[lc] < t_count[lc]:
                    have -= 1
                left += 1

        return shortest_string
                
            