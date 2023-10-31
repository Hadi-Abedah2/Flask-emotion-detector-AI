import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(url, json = myobj, headers=header)
    if resp.status_code == 400: 
        return {'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None,'dominant_emotion':None} 
    formatted_resp = json.loads(resp.text) # convert it to python dict
    anger = formatted_resp['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_resp['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_resp['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_resp['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_resp['emotionPredictions'][0]['emotion']['sadness']
    formatted_resp_dict = {'anger':anger, 'disgust':disgust, 'fear':fear, 'joy':joy, 'sadness': sadness}
    dominant_emotion = max(formatted_resp_dict, key=formatted_resp_dict.get) # max func to give the dominanat feeling
    formatted_resp_dict['dominant_emotion'] = dominant_emotion # update the dict with the dominant feeling
    return formatted_resp_dict