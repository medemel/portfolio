
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '46789090-wzfC2u9tZAa0bP54V2wLsAaLx4zwpfnPN5iGgREE'
ACCESS_SECRET = 'OehXoBROmK4Nfrl6AGP3iuEQqfUXjAP7Zya6SYaJZLo'
CONSUMER_KEY = '9zmZMdyYudLG8fBQktnJvw'
CONSUMER_SECRET = 'UyYhREyROkIuEpeRGSuWTOJDXSLLHYCZo05l67TBM'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

tweet_count = 10
for tweet in iterator:
    with open("sample_tweets.txt","w") as f:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter 
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        json.dump(tweet, f, indent=4)

        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break 

        f.close()