import tweepy #https://github.com/tweepy/tweepy
import csv

# Twitter APi
consumer_key = "b07lEq9VUdCXvkBxk8nzpTb5i"
consumer_secret = "Md6wi7Ru6rNZulexHln3W2PluMUAlBT6qMhptruIwWdQ1bcaoF"
access_key = "933741150783049733-etmbLMZrrl4oSURa4Hd1XV0eQxu2aS6"
access_secret = "XaiI8s3Sepvjep45Yfn1tPYtZVwWxr78ze1YePYj8LE5N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

#this function collects twitter profile tweets and returns Tweet objects
def get_tweets(screen_name):
    try:
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=20)
    except:
        user_profile = "broken"

#pull most popular

user = api.get_user('CitronResearch')
allTweets = api.user_timeline('CitronResearch',count=200)
maxRecount = 0
tweetid = 0
for tweet in allTweets:
if tweet.retweet_count > maxRecount:

print(tweet.retweet_count)
print(tweet.text)
