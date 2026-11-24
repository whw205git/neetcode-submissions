class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = {}

        for word in strs:
            sorted_word = self.sortWord(word)
            elements = grouped_words.get(sorted_word, [])
            elements.append(word)
            grouped_words[sorted_word] = elements
        return list(grouped_words.values())

    def sortWord(self, word: str) -> str:
        return ''.join(sorted(word))
        