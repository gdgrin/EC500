import tweepy
import wget

api_key = ''
api_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# tweets = api.search('landscape', count=200)
tweets = api.user_timeline(screen_name='caseymac',count=200, include_rts=False,exclude_replies=True)
media_files = set()
for tweet in tweets :
    media = tweet.entities.get('media', [])
    if(len(media) > 0) :
        media_files.add(media[0]['media_url'])

for media_file in media_files :
    wget.download(media_file, out = 'photos')

directory = 'photos'