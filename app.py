from flask import Flask, render_template, request, redirect, url_for
from random import randint
import requests
import json
import random as rnd
from random import getrandbits, shuffle
import string
from collections import OrderedDict
from operator import itemgetter

url = "https://codeforces.com/"


from flask import Flask, render_template

app = Flask(__name__)


def convert(number):
    word = ""
    dict = {
        "0": "zero ",
        "1": "one ",
        "2": "two ",
        "3": "three ",
        "4": "four ",
        "5": "five ",
        "6": "six ",
        "7": "seven ",
        "8": "eight ",
        "9": "nine "
    }
    for i in str(number):
        word += dict[i]
    return word


@app.route('/task2/avito/<gorod>/<vesh>/<xenya>')
def show_user_profile(gorod=None, vesh=None, xenya=None):
    adj = ["survellionisting", "abilluloidniy", "Asadulloichne"]
    verb = ["working", "torking", "sponking"]
    noun = ["thing", "dink", "jhhjh"]
    shuffle(adj)
    shuffle(verb)
    shuffle(noun)
    g1 = adj[0]
    g2 = verb[0]
    g3 = noun[0]
    return render_template('index.html', gorod=gorod, category=vesh, ad=xenya, a=g1, b=g2, c=g3)


@app.route('/task2/cf/profile/<username>/')
def boi(username):
    m = requests.get("https://codeforces.com/api/user.rating?handle=" + str(username)).json()
    if m["status"] != "OK":
        out = "User not found"
    else:
        print(m["result"])
        lol = str(m["result"][-1]["newRating"])
        out = """<table id=stats> <tr><th>User</th><th>Rating</th></tr>
<tr><td>{}</td><td>{}</td></tr>
</table>""".format(username, lol)
    return out


@app.route('/task2/num2words/<num>')
def num_work(num=None):
    num = int(num)
    if num > 999 or num < 0:
        status = "FAIL"
        return render_template("t2nums.html")
    else:
        if num % 2 == 0:
            iseven = "true"
        else:
            iseven = "false"

        num_text = convert(num)
        num_text.strip()

        return render_template("2tnumsR.html", num=num, iseven=iseven, num_text=num_text)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main page</title>
</head>
<body>
<ul>
    <li><h1>debug info</h1><a>city={{gorod}} category={{category}} ad={{ad}}</a></li>
    <li><h1>{{ad}}</h1></li>
    <li><a>{{a}} {{b}} {{c}}</a></li>

</ul>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Control work</title>
</head>
<body>

    <p>"status": "FAIL"</p>


</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bruhlord</title>
</head>
<body>


    <p>"status": "OK",</p>
    <p>"number": {{num}},</p>
    <p>"isEven": {{iseven}},</p>
    <p>"words": "{{num_text}}"</p>


</body>
</html>
