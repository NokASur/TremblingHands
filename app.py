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
    return render_template('av.html', gorod=gorod, category=vesh, ad=xenya, a=g1, b=g2, c=g3)


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


if __name__ == '__main__':
    app.run(host='127.0.0.6')
