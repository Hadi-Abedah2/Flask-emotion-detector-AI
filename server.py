''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion():
    ''' this funtion will take the textToAnalyze 
    from the query parameters and throw it to our
    pre-defined emotion_detector functions 
    '''
    inpt_text = request.args.get('textToAnalyze')
    dict_result = emotion_detector(inpt_text)
    anger = dict_result['anger']
    disgust = dict_result['disgust']
    fear = dict_result['fear']
    joy = dict_result['joy']
    sadness = dict_result['sadness']
    dominant_emotion = dict_result['dominant_emotion']

    if not dominant_emotion:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    ''' this function renders the template
    index.html 
    '''
    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True)
