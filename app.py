from flask import Flask, render_template, request
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


database_url = os.environ['DATA_BASE_URL'].split(':')
database_url = database_url[0] + "ql:" + ":".join(database_url[1:])
engine = create_engine(database_url)


Base = declarative_base()
Base.metadata.create_all(engine)
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class stupeeed_users(Base):
    __tablename__ = 'stupeed_users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(15), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)


app = Flask(__name__)


@app.route("/task5/sign-up", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("sign_in.html", CSK=os.environ['RECAPTCHA_SITE_KEY'])
    email = request.form['email']
    password = request.form['password']
    
if __name__ == '__main__':
    app.run()

