import heapq

class Twitter:
    
    def __init__(self):
        self.fdict = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.timestamp, tweetId))
        else:
            self.tweets[userId] = [(self.timestamp, tweetId)]
            self.follow(userId, userId)

        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        heap = []
        heapq.heapify(heap)
        following = self.fdict.get(userId)
        if not following:
            following = {userId}

        for followee in following:
            if followee in self.tweets:
                ind = len(self.tweets[followee]) - 1
                timestamp, tweet = self.tweets[followee][ind]
                heapq.heappush(heap, (timestamp, tweet, followee, ind))

        feed = []
        while len(heap) > 0 and len(feed) < 10:
            timestamp, tweet, followee, ind = heapq.heappop(heap)
            feed.append(tweet)
            next_ind = ind - 1
            if next_ind >= 0:
                new_time, new_tweet = self.tweets[followee][next_ind]
                heapq.heappush(heap, (new_time, new_tweet, followee, next_ind))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.fdict:
            self.fdict[followerId].add(followeeId)
        else:
            self.fdict[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.fdict[followerId]:
            self.fdict[followerId].remove(followeeId)
        
