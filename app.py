from flask import Flask, render_template
import requests
import inflect
import json
import random as rnd
import string
from random import shuffle


app = Flask(__name__)

s = rnd.choice(string.ascii_letters) + rnd.choice(string.ascii_letters)


@app.route('/task2/num2words/<num>/')
def numc(num):
    if int(num) < 0 or int(num) > 999:
        return json.dumps({"status": "FAIL"})
    else:
        p = inflect.engine()
        lol = p.number_to_words(int(num))
        if 'and' in lol:
            lol = ''.join(lol.split(' and'))
        if '-' in lol:
            lol = ' '.join(lol.split('-'))
        if int(num) % 2 == 0:
            m = True
        else:
            m = False
        return json.dumps({"status": "OK", "number": int(num), "isEven": m, "words": str(lol)})


@app.route('/task2/avito/<city>/<category>/<ad>/')
def avito(city, category, ad):
    out = """<h1>debug info</h1><p>city={} category={} ad={}</p><h1>{}</h1><p>{}</p>""".format(city, category, ad,
                                                                                                   category[1], city[1])
    return out


@app.route('/task2/cf/profile/<username>/')
def chelik(username):
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
