from flask import Flask, render_template, request
from flask_cors import CORS
from word_predictor import getWord, getSuggestedSentence, save_text

app = Flask(__name__, static_url_path='/static')
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/favicon.ico')
def staticdd():
    return app.send_static_file('favicon.ico')

@app.route('/sentence/<searchText>')
def getPredictedSentence(searchText):
    sentence = getSuggestedSentence(searchText)
    return sentence


@app.route('/save', methods=['POST'])
def saveData():
    print(str(request.data, "utf-8"))
    save_text(str(request.data, "utf-8"))
    return ""

if __name__ == '__main__':
    app.run()