"""Module providing JSON functionality."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('BX3vayi0hMwQdOo22rMOcPvC8_9Xbc6v82_axcO2TP4e')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/50c32bb2-e3af-470a-9294-92097dcc5b0a'
)


def english_to_french(english_text):
    ''' English to French Translator '''
    translation=language_translator.translate(text=english_text,model_id="en-fr").get_result()
    french_text=translation['translations'][0]['translation']
    print(json.dumps(french_text))
    return french_text

def french_to_english(french_text):
    ''' French to English Translator '''
    translation=language_translator.translate(text=french_text,model_id="fr-en").get_result()
    english_text=translation['translations'][0]['translation']
    print(json.dumps(english_text))
    return english_text
