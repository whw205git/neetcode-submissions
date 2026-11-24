from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            grouped_words[sorted_word].append(word)

        return list(grouped_words.values())

