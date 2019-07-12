import anvil.server
import os
from dotenv import load_dotenv
from watson_developer_cloud import NaturalLanguageClassifierV1

#This variable says which Natural Language Classifier to use later on in the code
#The whole os.getenv bit is because I save it to another file to keep my credentials safe and os.getenv goes and gets it out that file
model_id = os.getenv("NLC_model_id")

#This is like putting in the password for our specific instance of Natural Language Classifier
natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey=os.getenv("NLC_api_key"),
    url=os.getenv("NLC_url"),
)

@anvil.server.callable
def say_hello(name):
  print("Hello from the uplink, %s!" % name)

#this is my link you will need to update this value
anvil.server.connect('TKYP6FVKXCEZ5TEQ4K2ZE4TG-HVLZQDQTDXVZNU4A')



@anvil.server.callable
def add_text():
    response = natural_language_classifier.classify(model_id, 'this is a roaming inquiry').get_result()
    print(response)
    print(response['top_class'])
    return response['top_class']

anvil.server.wait_forever()
