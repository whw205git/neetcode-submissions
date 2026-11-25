
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # create a pattern map: {"*at": ["bat","rat"]}
        pattern_map = defaultdict(list)
        for word in wordList:
            for i, letter in enumerate(word):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

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
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for next_word in pattern_map[pattern]:
                        # found new word in wordList, add to queue
                        if next_word in word_set and next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)
            steps += 1

        return 0


