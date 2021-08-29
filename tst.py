from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'LOTwsKZCgu_0X1rJFbCeB8eFEKpWabaxxDIzRIKWVgob'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/4f97b2b2-53e4-422a-bff3-42832d24252e'

# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
with open('voice_sample.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

text = res['results'][0]['alternatives'][0]['transcript']
confidence = res['results'][0]['alternatives'][0]['confidence']
with open('output.txt', 'w') as out:
    out.writelines(text)


# -------------------

from ibm_watson import TextToSpeechV1

apikey2 = 'XkYm1sSQZXMSyd5tDG_LuKlZ5LvaDES2CcIdSAtqE9SN'
url2 = 'https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/2d4dcf18-d101-4910-91df-808e8f435382'

# Setup Service
authenticator2 = IAMAuthenticator(apikey2)
tts = TextToSpeechV1(authenticator=authenticator2)
tts.set_service_url(url2)

with open('output.txt', 'r') as f:
    text = f.readlines()

text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)

with open('speech.wav', 'wb') as audio_file:
    audio_file.write(
        tts.synthesize(
            text,
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)