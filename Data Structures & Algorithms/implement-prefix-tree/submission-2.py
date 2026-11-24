class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_eow = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_eow

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        
    def _find(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

