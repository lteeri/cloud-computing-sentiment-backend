from flask import Flask
import pickle

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
    return "<p>Hello, World!</p>"