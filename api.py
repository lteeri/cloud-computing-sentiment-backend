from flask import Flask, request
import pickle

import os

testing_env_var = os.environ.get("ANOTHER-ENV-VARIABLE", "This is in api.py")
debug_env = os.environ.get("DEBUG")
host_ip_env = os.environ.get("HOST-IP")

app = Flask(__name__)

# bringing the sentiment analysis tool into the backend using pickle
with open("sentiment_model_sklearn_1.6.1.pkl", "rb") as file:
    sentiment_model = pickle.load(file)

print(type(sentiment_model))

print("should be positive: ", sentiment_model.predict(["Today was a great day."]))
print("should be neutral: ", sentiment_model.predict(["I have strated building the backend."]))
print("should be negative: ", sentiment_model.predict(["Some day my dog will die."]))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" f"<p>Testing env variable: {testing_env_var}</p>" \
    f"<p>Debug mode: {debug_env}</p>" f"<p>Debug mode: {host_ip_env}</p>"


@app.route("/analysis", methods=['POST'])
def sentiment_analysis():
    req = request.get_json()

    print("req data: ", req)

    # if there is no request data, we can do an early return
    if req is None:
        return "No JSON received", 400

    # if there is data, we move here
    # let's do the sentimnt analysis
    analysis = sentiment_model.predict([req["sentence"]])
    print(analysis)

    # a small error check for if the analysis list is empty
    if analysis is None:
        return "Analysis couldn't be done. Please try again."
    
    # the analysis looks like this ['positive'] so we want the index 0 word out
    result = analysis[0]
    return {"analysis": result}
