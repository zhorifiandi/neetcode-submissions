from heapq import heappush, heappop

class Twitter:

    def __init__(self):

        # key: userId, value: set of userID s
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

        # key: userId, value: heap of tweets
        self.newsFeedSize = 10
        self.newsFeed = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        candidates = []
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                followeeTweets = self.tweets[followeeId]
                index = len(followeeTweets) - 1
                ts, tweetId = followeeTweets[index]
                heappush(candidates, (ts, tweetId, followeeId, index - 1))

        result = []
        while candidates and len(result) < self.newsFeedSize:
            ts, tweetId, followeeId, nextIndex = heappop(candidates)
            if followeeId in self.following[userId]:
                result.append(tweetId)
            
            if nextIndex >= 0:
                ts, nextTweetId = self.tweets[followeeId][nextIndex]
                heappush(candidates, (ts, nextTweetId, followeeId, nextIndex - 1))

        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
