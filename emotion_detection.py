import json
import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, data=json.dumps(input_json))
    
    emotion_results = json.loads(response.text)

    user_emotion = emotion_results['emotion_predictions'][0]['emotion']
    anger = user_emotion['anger']
    disgust = user_emotion['disgust']
    fear = user_emotion['fear']
    joy = user_emotion['joy']
    sadness = user_emotion['sadness']

    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }
    final_result = max(scores, key=scores.get)
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': final_result
    }