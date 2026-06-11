class Twitter:
    
    def __init__(self):
        self.fdict = {}
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId, tweetId))

        if userId not in self.fdict:
            self.follow(userId, userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        
        feed = []
        following = self.fdict.get(userId)
        if not following:
            following = {userId}

        i = 1
        while i <= len(self.posts) and len(feed) < 10:
            user, tweet = self.posts[-i]
            if user in following:
                feed.append(tweet)
            i += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.fdict:
            self.fdict[followerId].add(followeeId)
        else:
            self.fdict[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.fdict[followerId]:
            self.fdict[followerId].remove(followeeId)
        
