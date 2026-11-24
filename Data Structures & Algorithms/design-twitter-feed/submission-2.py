
class Twitter:

    def __init__(self):
        self.timestamp = 0
        # key is followerId, value is set of followeeIds
        self.follow_map = defaultdict(set)
        # key is userId, value is all tweets (timestamp, tweet ID)
        self.tweets = defaultdict(list)  
        self.max_feed_size = 10      

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_users = {userId}.union(self.follow_map[userId])
        
        max_heap = []
        for user in all_users:
            if self.tweets[user]:
                # push the most recent tweet into heap
                idx = len(self.tweets[user]) - 1
                timestamp, tweetId = self.tweets[user][idx]
                heapq.heappush_max(max_heap, (timestamp, tweetId, user, idx-1))

        feed = []
        while max_heap and len(feed) < self.max_feed_size:
            timestamp, tweetId, user, prev_idx = heapq.heappop_max(max_heap)
            feed.append(tweetId)

            if prev_idx >= 0:
                timestamp, tweetId = self.tweets[user][prev_idx]
                heapq.heappush_max(max_heap, (timestamp, tweetId, user, prev_idx-1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
