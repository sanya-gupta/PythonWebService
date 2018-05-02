'''from twython import Twython
    
    APP_KEY = "uyRwkSCq6KOtXJyMcImiiLwFn"
    APP_SECRET = "WoBoP7mQx8OfDxfQM9aPWCuzQ9p66M2i4Ihn3ffL36lLnYYJH6"
    OAUTH_TOKEN = "36549219-6Z847rAgZwRchfH1S7Po2GLFf3Ibxafhbm0o8wd4l"
    OAUTH_TOKEN_SECRET = "fyiaVB08mSLIQWYoHsFL4qHHyyAmBtSiYalad5Nc4fyoI"
    
    twitter = Twython(APP_KEY, APP_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    twitter.verify_credentials()
    twitter.get_home_timeline()
    twitter.update_status(status='Status updated using Twython API')
    '''

import tweepy

consumer_token = "uyRwkSCq6KOtXJyMcImiiLwFn"
consumer_secret = "WoBoP7mQx8OfDxfQM9aPWCuzQ9p66M2i4Ihn3ffL36lLnYYJH6"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print( "Error! Failed to get request token." )

print( redirect_url )

verifier = input('Verifier:')

try:
    auth.get_access_token( verifier )
except tweepy.TweepError:
    print( "Error! Failed to get access token." )

new_token = auth.access_token
new_secret = auth.access_token_secret


