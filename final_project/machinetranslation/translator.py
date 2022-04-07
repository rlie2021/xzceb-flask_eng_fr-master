#import json
import os
from pandas import json_normalize
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3



# Get environment variables
apikey = os.getenv('API_KEY')
url = os.environ.get('API_URL')

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

json_normalize(
    language_translator.list_identifiable_languages().get_result(), "languages")

load_dotenv()

# Function to convert english to french
def english_to_french(english_text):
    french_translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = french_translation['translations'][0]['translation']
    return french_text

# Function to convert french to english
def french_to_english(french_text):
    english_translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = english_translation['translations'][0]['translation']
    return english_text
