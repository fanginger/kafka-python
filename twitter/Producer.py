from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

access_token = "1374962236268011527-Sq8FGmgrQKg7UWUBZ45APJ3i6xGTUo"
access_token_secret =  "FR0iLx3X30A02noj17sTyIA7SjVRiI1koEwbPu8LsqTAv"
consumer_key =  "PGaMPGZRohVjkymFpkvjYewBm"
consumer_secret =  "8LRHmvRrSzvnDUAc9l90sLnZsz1aCnBr4MEDRQ6pdv4mgl6xAI"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)
l = StdOutListener() 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l) # 接近即時的資料
stream.filter(track="trump") # 取資料: 篩選特定字詞