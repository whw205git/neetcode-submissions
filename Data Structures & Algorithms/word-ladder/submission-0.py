
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)        
        visited = set(beginWord)

        queue = deque([beginWord])
        steps = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps

                # get next words
                for i, char in enumerate(word):
                    for letter in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i] + letter + word[i+1:]
                        # found new word in wordList, add to queue
                        if next_word in word_set and next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)
            steps += 1

        return 0


