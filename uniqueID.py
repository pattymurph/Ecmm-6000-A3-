import tweepy
import time 


# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
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

    s = get_all_tweets("CitronResearch")
    print "Name:" + s.name
    print "Location:" + s.location
    print "Description:" + s.description
