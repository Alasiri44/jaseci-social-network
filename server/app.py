from flask import make_response
from __init__ import create_app

app = create_app()

@app.route('/')
def index():
    return make_response('<h1>Welcome to the social network backend</h1>')

if __name__ == '__main__':
    app.run(debug=True)