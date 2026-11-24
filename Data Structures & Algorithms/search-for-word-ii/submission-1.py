class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"

        # build a trie where EOW is indicated by {$: word}
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        rows, cols = len(board), len(board[0])
        found_words = []

        def backtrack(r: int, c: int, parent: dict):
            letter = board[r][c]
            curr_node = parent[letter]

            # check if we found a complete word
            word_match = curr_node.pop(WORD_KEY, False)
            if word_match:
                found_words.append(word_match)

            # mark visited in place
            board[r][c] = "#"

            # check each of the four directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    backtrack(nr, nc, curr_node)

            # reset the letter
            board[r][c] = letter

            # optimization to prune leaf nodes from trie, so if a word is already found, don't try to find it again.
            # if not curr_node:
            #    parent.pop(letter)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    backtrack(r, c, trie)
        return found_words


        