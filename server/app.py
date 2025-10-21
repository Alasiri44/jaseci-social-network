from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return make_response('<h1>Welcome to the social network backend</h1>')