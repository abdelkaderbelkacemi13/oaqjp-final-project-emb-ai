from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/")
def home():
    return render_template("template/index.html")


@app.route("/detect_emotion", methods=["Get","POST"])
def emotiondetector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_result = emotion_detector(text_to_analyze)
    
    
    anger = emotions_result['anger']
    disgust = emotions_result['disgust']
    fear = emotions_result['fear']
    joy = emotions_result['joy']
    sadness = emotions_result['sadness']
    dominant_emotion = emotions_result['dominant_emotion']
    
    return f"For the given statement, the system response is " \
       f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
       f"'joy': {joy}, and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)