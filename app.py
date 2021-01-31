from flask import Flask, render_template, request, redirect, url_for
from random import randint
import requests
import inflect
import json
import random as rnd
from random import getrandbits, shuffle
import string
from collections import OrderedDict
from operator import itemgetter


app = Flask(__name__)

s = rnd.choice(string.ascii_letters) + rnd.choice(string.ascii_letters)

s = rnd.choice(string.ascii_letters) + rnd.choice(string.ascii_letters)

value_ = {
    "token": "4UffYATBFJOqTiy9aJDnajwBa5XrSTfy",
    "secret": "sufgsfsugfssef3432424242423424242",
    "command": "set",
    "key": "",
    "value": ""
}
data_set = value_

key_ = {
    "token": "4UffYATBFJOqTiy9aJDnajwBa5XrSTfy",
    "secret": "sufgsfsugfssef3432424242423424242",
    "command": "get",
    "key": ""
}
data_get = key_

games_info = {}


@app.route("/task4/santa/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        create_form = request.form
        game_name = str(create_form["name_of_game"])
        game_code = str(getrandbits(64)) + game_name
        game_code_secret = str(getrandbits(64))
        link_for_player = "/task4/santa/play/{link}".format(link=game_code)
        link_for_organizers = "/task4/santa/toss/{link}/{secret}".format(link=game_code, secret=game_code_secret)
        info = {"name": game_name, "code": game_code, "secret": game_code_secret, "play": link_for_player,
                "organize": link_for_organizers, "active": "True", "players": []}
        data_set["key"] = game_code
        data_set["value"] = json.dumps(info)
        requests.post("https://arsenwisheshappy2021.herokuapp.com/query", data=data_set)
        return render_template("create_posted.html", form=create_form, player_link=link_for_player,
                               organizer_link=link_for_organizers)
    else:
        return render_template('create_form.html')


@app.route('/task3/cf/profile/<handle>/')
def cf_si(handle):
    return redirect(url_for('cf_single', handle=handle, page_number=1))


@app.route('/task3/cf/profile/<handle>/page/<int:page_number>/')
def cf_single(handle, page_number):
    url = f'http://codeforces.com/api/user.status?handle={handle}&from=1&count=100'
    text = requests.get(url).text
    line = json.loads(text)
    popitki = line["result"]

    max_page_number = (len(popitki) + 24) // 25
    return render_template("sing.html", popitki=popitki, handle=handle, max_page_number=max_page_number,
                           page_number=page_number)


@app.route('/task3/cf/top/')
def top():
    handles = sorted(request.args.get("handles").split("|"))
    orderby = request.args.get("orderby", "")
    handict = {}
    url = "https://codeforces.com/api/user.info?handles="
    for nick in handles:
        url = url + nick + ";"
    ssilka = json.loads(requests.get(url).text)
    if ssilka["status"] == "FAILED":
        return "User not found"
    else:
        for nick in ssilka["result"]:
            handle = nick["handle"]
            rating = nick["rating"]
            handict[handle] = int(rating)
        if orderby == "rating":
            handict = OrderedDict(sorted(handict.items(), key=itemgetter(1), reverse=True))
    return render_template("Top.html", dict=handict)


@app.errorhandler(404)
def mistake(succ):
    return render_template("error.html"), 404


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
