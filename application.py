from flask import Flask
from flask_cors import CORS
from word_predictor import getWord, getSuggestedSentence

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/word/<searchText>')
def getSuggestionWord():
    return getWordList()


@app.route('/sentence/<searchText>')
def getPredictedSentence(searchText):
    sentence = getSuggestedSentence(searchText)
    return sentence