from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/haba')
def hello_world():
    text = 'Hello Haba!\nHello Arsen!\nHello Karim!'
    return f'<pre>{text}</pre>'

