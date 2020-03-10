import tweepy
from time import sleep
from credentials import *


# Access & authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Follow everyone that follows the bot
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


# For loop to iterate over tweets with #freeCodeCamp, limit to 10
terms = '#freeCodeCamp OR #100DaysofCode OR #CodeNewbie OR #Python OR #IoT OR #JavaScript OR #Linux OR #Programming'
for tweet in tweepy.Cursor(api.search,
                           q=terms).items():
    
    # Print out usernames of the last 10 people to use #freeCodeCamp
    try:
        print('Tweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        tweet.favorite()
        print("Favorited the tweet")

        if not tweet.user.following:
            tweet.user.follow()
            print("Followed the user")
        sleep(600)

    except tweepy.TweepError as e:
        print(e.reason)
    except:
        StopIteration
        break

