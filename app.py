from flask import Flask, render_template, request, url_for, session,redirect
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix
import json, os, psycopg2, smtplib
from datetime import datetime

database_url = os.environ['DATABASE_URL'].split(':')
database_url = database_url[0] + "ql:" + ":".join(database_url[1:])
engine = create_engine(database_url)


Base = declarative_base()
Base.metadata.create_all(engine)
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

conn = psycopg2.connect(database_url)
cur = conn.cursor()


class stupeeed_users(Base):
    __tablename__ = 'stupeed_users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(15), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)


app = Flask(__name__)


@app.route("/")
def index1():
    return "balls"


@app.route("/task5/sign-in", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("sign_in.html", CSK=os.environ['RECAPTCHA_SITE_KEY'])
    email = request.form['email']
    password = request.form['password']
    cur.execute(f"SELECT COUNT(*) FROM users WHERE email = '{email}'")
    count = cur.fetchall()[0][0]
    if count == 0:
        return render_template("sign-in.html", error=True)
    cur.execute(f"SELECT password FROM users WHERE email = '{email}'")
    password_hash = cur.fetchall()[0][0]
    if not check_password_hash(password_hash, password):
        return render_template("sign-in.html", error=True)
    time = datetime.now()
    session['email'] = email
    cur.execute(f"INSERT INTO ips (email, ip, time) VALUES ('{email}', '{request.remote_addr}', '{time}')")
    conn.commit()
    session['auth'] = 'logged'
    return redirect(url_for('account'))

