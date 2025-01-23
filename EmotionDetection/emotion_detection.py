import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert the response text into a dictionary
    emotions_dict = json.loads(response.text)
    
    # Access the emotions from the nested structure
    if 'emotionPredictions' in emotions_dict and len(emotions_dict['emotionPredictions']) > 0:
        emotions = emotions_dict['emotionPredictions'][0]['emotion']
    else:
        print("No emotions found in the response.")
        return None
    
    # Extract the emotions and their scores
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format the output
    formatted_output = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    
    return formatted_output

# Example usage
text = "I am so happy and excited about the new project!"
result = emotion_detector(text)
print(result)