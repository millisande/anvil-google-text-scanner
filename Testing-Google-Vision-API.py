from google.cloud import vision
import json
#from google.oauth2 import service_account

#Run this in command line first
#export GOOGLE_APPLICATION_CREDENTIALS="service.json"s

client = vision.ImageAnnotatorClient()

with open('./image.jpg', 'rb') as image_file:
    content = image_file.read()
    response = client.document_text_detection({'content': content})
    print(response.full_text_annotation.text)
