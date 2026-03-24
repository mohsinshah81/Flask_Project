import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP EmotionPredict API
    and returns the 'text' attribute from the response.
    """
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

      # Build the input JSON
    Json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request
    response = requests.post(url, headers=Headers, json=Json)

   # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        emotions = None
        dominant_emotion = None
    else:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
    print(emotions)
    print(dominant_emotion)

    return {
        "emotions": emotions,
        "dominant_emotion": dominant_emotion
    }
