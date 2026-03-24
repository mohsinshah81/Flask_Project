from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emotions = response['emotions']
    dominant_emotion = response['dominant_emotion']
    if emotions is None:
        return "Invalid input! Try again."
    else:
        return f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}"
 
@app.route("/")
def render_index_page():
    return render_template('index.html')


# Run the Flask app
if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(host="0.0.0.0", port=5000)