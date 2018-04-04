import tweepy
import wget

import io
import os

import subprocess

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

api_key = '07J6DTOfFNVvROefk2L4X3EPi'
api_secret = 'y7zBiXCN8wSV8Uhn4wlYFjgxxFzRAasCpUEgD5jrx9QYFhnGgb'
access_token = '4108052595-kCEtiUcDB2zeRqjn61wJqbsO1ZJ8jLwQRw7s1zR'
access_secret = 'frHKcMR2mcy54NEHyv0eZ4yChoc4eB75ls4akvutoWp8O'

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

directory = 'photos'

if not os.path.exists(directory):
    os.makedirs(directory)

handle = raw_input("Enter Twitter Handle: \n ")

# tweets = api.search('landscape', count=200)
tweets = api.user_timeline(screen_name=handle,count=200, include_rts=False,exclude_replies=True)
media_files = set()
for tweet in tweets :
    media = tweet.entities.get('media', [])
    if(len(media) > 0) :
        media_files.add(media[0]['media_url'])

if(len(media_files) == 0):
    print "No Images Found"
    quit()

for media_file in media_files :
    wget.download(media_file, out = 'photos')


j=0
def image_rename():
    j=0
    directory = "photos"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            os.rename(directory + "/" + filename, directory + "/image" + str(j) + ".jpg")
            j+=1
    return
i=0
image_rename()

def filecount(dir_name):
     return len([f for f in os.listdir(dir_name) if os.path.isfile(f)])

numFiles = filecount(os.getcwd())

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
i=0
while i < numFiles:
    file_name = os.path.join(
        os.path.dirname(__file__),
        'photos/image{}.jpg'.format(i))

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    file = open("descriptions.txt","a")

    for label in labels:
        file.write(label.description)
        file.write("\n")

    i+=1
i=0
# create video
fps = 1
subprocess.call(["ffmpeg","-y","-r",str(fps),"-i", "photos/image%d.jpg","-vcodec","mpeg4", "-qscale","20", "-r", str(fps), "video.avi"])