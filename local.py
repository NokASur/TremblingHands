from flask import Flask
import random as rnd

app = Flask(__name__)


@app.route('/task1/random/')
def hello_world():
    text = "Haba's mark is " + str(rnd.randint(1, 5))
    return f'<pre>{text}</pre>'


@app.route('/task1/i_will_not/')
def hello_world1():
    text = "<li>I will not waste time</li>\n" * 100
    return f'<ul>{text}</ul>'


@app.route('/')
def hello_world2():
    text = "<li><a href='/task1/random/'>/task1/random/</a></li>\n" \
           "<li><a href='/task1/i_will_not/'>/task1/i_will_not/</a></li>"
    return f'<ul>{text}</ul>'


if __name__ == '__main__':
    app.run(host='127.0.0.6')
