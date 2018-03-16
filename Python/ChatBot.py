#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)


@app.route('/')
def chat():
    return render_template('ChatBot.html')


@app.route('/receiver', methods=['POST'])
def usermsg():
    data = request.get_json()
    msg = data['msg']
    print(msg)
    return json.dumps({'status': 'OK', 'msg': msg})


app.run()