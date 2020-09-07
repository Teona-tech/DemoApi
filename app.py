from flask import Flask, redirect
from flask_restful import Api

from resources.methods import TemSentenceTokenizer

app = Flask(__name__)

api = Api(app)

@app.route('/')
def home():
    return redirect('https://github.com/temurchichua/DemoApi')

api.add_resource(TemSentenceTokenizer, '/TemSenTok')

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
