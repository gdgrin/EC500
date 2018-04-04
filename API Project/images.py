import tweepy
import wget

api_key = '07J6DTOfFNVvROefk2L4X3EPi'
api_secret = 'y7zBiXCN8wSV8Uhn4wlYFjgxxFzRAasCpUEgD5jrx9QYFhnGgb'
access_token = '4108052595-kCEtiUcDB2zeRqjn61wJqbsO1ZJ8jLwQRw7s1zR'
access_secret = 'frHKcMR2mcy54NEHyv0eZ4yChoc4eB75ls4akvutoWp8O'

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


handle = raw_input("Enter Twitter Handle: \n ")

# tweets = api.search('landscape', count=200)
tweets = api.user_timeline(screen_name=handle,count=200, include_rts=False,exclude_replies=True)
media_files = set()
for tweet in tweets :
    media = tweet.entities.get('media', [])
    if(len(media) > 0) :
        media_files.add(media[0]['media_url'])

for media_file in media_files :
    wget.download(media_file, out = 'photos')

directory = 'photos'