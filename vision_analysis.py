#Source: https://cloud.google.com/vision/docs/reference/libraries#client-libraries-install-python

import io
import os


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