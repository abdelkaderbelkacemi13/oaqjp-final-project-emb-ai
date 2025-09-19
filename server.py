from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotiondetector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_result = emotion_detector(text_to_analyze)
    
    
    anger = emotions_result['anger']
    disgust = emotions_result['disgust']
    fear = emotions_result['fear']
    joy = emotions_result['joy']
    sadness = emotions_result['sadness']
    dominant_emotion = emotions_result['dominant_emotion']
    
    formatted_output = (
    f"For the given statement, the system response is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} "
    f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")
    
    return formatted_output
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)