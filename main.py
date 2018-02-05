import tweepy
import wget

import io
import os

import subprocess

api_key = ''
api_secret = ''
access_token = ''
access_secret = ''

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

def image_rename():
    i=0
    directory = "photos"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            os.rename(directory + "/" + filename, directory + "/image" + str(i) + ".jpg")
            i+=1
    return

image_rename()

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
i=2
while i < 10 :
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

fps = 1
subprocess.call(["ffmpeg","-y","-r",str(fps),"-i", "photos/image%d.jpg","-vcodec","mpeg4", "-qscale","5", "-r", str(fps), "video.avi"])