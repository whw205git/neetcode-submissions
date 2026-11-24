class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, idx: int):
            if idx == len(word):
                return True

            if not(0 <= r < rows and 0 <= c < cols and board[r][c] == word[idx]):
                return False

            letter = board[r][c]
            board[r][c] = "#"

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if backtrack(nr, nc, idx+1):
                    return True

            board[r][c] = letter

            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
        