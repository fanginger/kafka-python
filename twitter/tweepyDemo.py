import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

access_token = "1374962236268011527-Sq8FGmgrQKg7UWUBZ45APJ3i6xGTUo"
access_token_secret =  "FR0iLx3X30A02noj17sTyIA7SjVRiI1koEwbPu8LsqTAv"
consumer_key =  "PGaMPGZRohVjkymFpkvjYewBm"
consumer_secret =  "8LRHmvRrSzvnDUAc9l90sLnZsz1aCnBr4MEDRQ6pdv4mgl6xAI"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get user posts
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.get_user('twitter')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

class StdOutListener(StreamListener): # 繼承
    def on_status(self, status):
        print(status.text)

l = StdOutListener() 
stream = Stream(auth,l) # 接近即時的資料
# stream.register(TweetViewer(limit=3 ))  # 設定使用瀏覽or寫入檔案 
stream.filter(track="trump") # 取資料: 篩選特定字詞