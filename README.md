# anvil-google-scanner-text
A project to work with anvil's free tier to run OCR on a picture with google's text scanner

This was an attempt at an anvil/python version of the [starter-google-text-scanner app](https://github.com/millisande/starter-google-text-scanner).

[Anvil](https://anvil.works/?utm_expid=97990206-5.gXkeODHgSXWSbT--IBAoUQ.0&utm_referrer=https%3A%2F%2Fwww.google.com%2F) is a drag and drop UI creator which is coded together using python.

We will also be running code on our local server to run the API calls to Google or IBM's Natural Language Classifier service.

If you pay for Anvil's higher tiers you could run all these API calls from the python code in the Anvil app. However, because this app was created as an educational tool, and just a prototype, we intended to only run the code locally and not use the paid for service. To be able to make an app which can do the API calls even if you are not on the same wifi network as the local server which runs the API calls you would need to write the API calls directly into the Anvil UI editor.

## How to create an anvil app

First you would need to download the app file (named App ) 
Then youb will need to go to "My Apps " on the "Anvil" website and click on the "import from file " button (just below the "create app" button) and select the app file.
You should eventually see the app in "Anvil" 

!["Import .yaml file "](/readme-images/import-app-sc.png "Import .yaml file")

## How to run the local part of the app

### How to install the packages we need to run the app

We are going to use pipenv to section off the bit of the computer we are working in so that our dependencies for this program do not intefere with other projects. You can see instructions on how to install [pipenv here](https://pypi.org/project/pipenv/).

The first time you run this code you will need to run:

`pipenv --three`

This is to instantiate the pipenv and tell it to use Python version 3 (Python 2 is the default on macs).

Then run:

`pipenv install --dev`

This will install all of the packages that the Pipfile specifies that we need. If you are not currently in the Day 1 folder in your command line then this will not install the packages you need to run the python code.

Then run:


`pipenv shell`

This will open the virtual environment that we've saved all the packages to so that we can use them.

### Get an IBM classifier and add the credentials to the application

If you wish to use the IBM classifier service to classify some text and present it in the anvil website you will need to set up a classifier and then add the credentials to access it to this application.


You will need to sign up for [IBM cloud](cloud.ibm.com).

Then you will need to go the catalog and search for `Natural Language Classifier` and set up a service. 

Open a file in your code editor of choice, paste this in:

```
NLC_api_key=WHATEVER-YOUR-NLC-API-KEY-IS
NLC_model_id=WHATEVER-YOUR-MODEL-ID-IS
NLC_url=WHATEVER-YOUR-CLASSIFIER-SERVICE-END-POINT-IS
```

Replace the capitalised words on the right hand side of the equals sign on both rows with the actual values of your api key and your model id. You can find your api key on the IBM Cloud page for your NLC and NLU service respectively, the page with the "Launch Tool" button for NLC. You can find your model id on the Overview page when you click to test your model in the GUI.

Your url will be different depending on where you decided to host your Natural Language Classifier and Natural Language Understanding services. You can see the list of which url to use for which region(for NLC here)[https://cloud.ibm.com/apidocs/natural-language-classifier#service-endpoint].

Save the file as `.env`

### Get a Google OCR text scanner service and add the credentials to the application

Actually the file that is called `Testing-Google-Vision-API.py` doesn't actually connect to Anvil. It does however connect to Google and is an example of how you would do this API call in python code.

You need to sign up for a Google Cloud Account. [Sign up for the free trial](https://cloud.google.com/free/docs/gcp-free-tier).

Open the API tab Library from the left hand menu of the Google Cloud Dashboard.

![Open API Library](/readme-images/look-for-API.png "Open API Library")

Use the search bar to find the Cloud Vision API. Add that api to a (new) project.

![Find Cloud Vision API](/readme-images/find-cloud-API.png "Find Cloud Vision")

Go to the credentials tab and choose to Create a new service.

![Set up new credentials](/readme-images/API-credentials-page.png "Set up new credentials")

You will need to create a Service Account Key. Choose to create the key for the project you made and associated with the Cloud API call.

![Create service key](/readme-images/create-service-key.png "Create service key")

This will create a .json file, it should automatically download to your computer. Take that file and move it to the folder with this code.

Rename the file to `service.json`

### Running the application

In order for anvil to be able to call the APIs you will need to have your local application running for the entire period where you want to anvil app to work.

If you are doing the natural language classifier version (this is set up to use Anvil whereas the other code is not) you need only to use the command `python Testing-Anvil-Classifier.py`. You can then open the Anvil app in your browser.

If you are doing the Google API calls then you will need to first run in the command line:

If you are on a Mac then run:

```
export GOOGLE_APPLICATION_CREDENTIALS="service-key.json"
```

If you are on a Windows machine then run:

```
set GOOGLE_APPLICATION_CREDENTIALS=service-key.json
```

Then you can run `python Testing-Google-Vision-API.py` to run the google vision recognition.

## Outstanding work

The Testing-Google-Vision-API could be made callable by anvil.
