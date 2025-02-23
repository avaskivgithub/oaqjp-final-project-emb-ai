from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    result = "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}".format(response['anger'],
                                                                                                                      response['disgust'],
                                                                                                                      response['fear'],
                                                                                                                      response['joy'],
                                                                                                                      response['sadness'],
                                                                                                                      response['dominant_emotion'])

    # If results are None
    result_detector = "For the given statement, the system response is {}.".format(result)
    # If None then just error message
    if response['dominant_emotion'] is None:
        result_detector = "Invalid text! Please try again!"

    return result_detector

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)