import os

# This function posts a tweet
def post_tweet(account, tweet):
    # Import the necessary methods from tweepy library
    from tweepy.auth import OAuthHandler
    from tweepy import API
    from tweepy import Cursor
    import tweepy

    # Twitter API credentials
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    access_key = os.environ.get("TWITTER_ACCESS_KEY")
    access_secret = os.environ.get("TWITTER_ACCESS_SECRET")
    # print all 4 above variables
    print(consumer_key, consumer_secret, access_key, access_secret)
    # Create an OAuthHandler object
    auth = OAuthHandler(consumer_key, consumer_secret)
    # Set access token and secret
    auth.set_access_token(access_key, access_secret)
    # Create API object
    api = API(auth)
    # Try to post the tweet
    try:
        resp = api.update_status(tweet)
        print("Tweet posted successfully!")
        print(resp)
    # If there is an error, print it
    except tweepy.errors.TweepyException as e:
        print(e)
    # print a link to the tweet
    print(
        "https://twitter.com/{}/status/{}".format(
            account, api.user_timeline(screen_name=account)[0].id
        )
    )


# if main then post_tweet()
if __name__ == "__main__":

    # Get the account name and tweet from the user
    account = "TheHeroShep"
    # tweet = input("Enter the tweet: ")
    tweet = "Testing the Twitter API, Tweepy, & github copilot - response this time."
    # Post the tweet
    post_tweet(account, tweet)
