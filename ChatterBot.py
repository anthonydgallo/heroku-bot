# Dependencies
import tweepy
import time
import os

# Quotes to Tweet
quote_list = [
    "Quote 1",
    "Quote 2",
    "Quote 3"]


# Create function for tweeting
def QuoteItUp(quote_num):

    # Twitter credentials
    auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
    auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the next quote
    api.update_status(quote_list[quote_num])

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
counter = 0

while(counter < len(quote_list)):
    QuoteItUp(counter)
    counter = counter + 1
    time.sleep(15)
