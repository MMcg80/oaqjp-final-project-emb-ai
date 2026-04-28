import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # If the response status code is 200, extract emotions and their score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        
        dominant_emotion = max(emotions, key=emotions.get)

    # If the response status code is 400, set label and score to None   
    elif response.status_code == 400:
		anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    
    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    if dominant_emotion == None:
        return "Invalid text. Please try again!"

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
	

# result = emotion_detector("I am so happy this . works!")
# print(result['dominant_emotion']) 