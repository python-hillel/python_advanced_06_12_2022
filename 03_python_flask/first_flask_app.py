from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!<br>My first application!</h1>'


app.run(debug=True, port=12345)
