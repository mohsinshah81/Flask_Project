from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")


@app.route("/EmotionDetector")
def sent_analyzer(): 
    # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')

# Pass the text to the sentiment_analyzer function and store the response 
    response = emotion_detector(text_to_analyze)

# Extract the emotion and score from the response 


# Return a formatted string with the emotions and score 


@app.route("/")
def render_index_page():
    return render_template('index.html')
    
    if name == "main":
        app.run(host="0.0.0.0", port=5000)