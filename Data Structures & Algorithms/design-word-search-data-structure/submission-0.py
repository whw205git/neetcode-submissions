class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_eow = True

    def search(self, word: str) -> bool:
        return self._find(word, 0, self.root)

    def _find(self, word: str, idx: int, node: TrieNode) -> bool:
        if idx == len(word):
            return node.is_eow   
        char = word[idx]
        if char == '.':
            # any children would match
            for child in node.children.values():
                if self._find(word, idx+1, child):
                    return True
            return False
        else:
            # match specific char
            return char in node.children and self._find(word, idx+1, node.children[char])