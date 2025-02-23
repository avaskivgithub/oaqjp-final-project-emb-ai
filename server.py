"""Emotion Detection web app."""

from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """Main app route."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    result = "".join([
                    f"'anger': {response['anger']}, ",
                    f"'disgust': {response['disgust']}, ",
                    f"'fear': {response['fear']}, ",
                    f"'joy': {response['joy']} ",
                    f"and 'sadness': {response['sadness']}. ",
                    f"The dominant emotion is {response['dominant_emotion']}"
                    ])

    # If results are None
    result_detector = f"For the given statement, the system response is {result}."
    # If None then just error message
    if response['dominant_emotion'] is None:
        result_detector = "Invalid text! Please try again!"

    return result_detector

@app.route("/")
def render_index_page():
    """Rendering of the main application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
