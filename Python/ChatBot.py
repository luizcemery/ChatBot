#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json, watson_developer_cloud

# Set up Conversation service.
conversation = watson_developer_cloud.ConversationV1(
  username = '2f6399a7-e75b-4018-9668-870042d1d71f', # replace with username from service key
  password = 'wPM2aoaExw4b', # replace with password from service key
  version = '2017-05-26'
)
workspace_id = '389a07ea-70d7-40eb-92c4-0ab75122bfff' # replace with workspace ID

# Initialize with empty value to start the conversation.
user_input = ''

app = Flask(__name__)

user_input = ''
def update_context(contexto):
    global user_context
    user_context = contexto

def get_context():
    global user_context
    return user_context

@app.route('/')
def chat():
    response = conversation.message(
        workspace_id=workspace_id,
        input={
            'text': user_input
        }
    )

    update_context(response['context'])
    return render_template('ChatBot.html')


@app.route('/receiver', methods=['POST'])
def usermsg():
    data = request.get_json()
    user_input = data['msg']

    response = conversation.message(
        workspace_id=workspace_id,
        input={
            'text': user_input
        },
        context = get_context()
    )

    update_context(response['context'])

    if response['intents']:
        print(response)
        intent = response['intents'][0]['intent']
        msg = response['output']['text'][0]
    else:
        intent = ''
        msg = response['output']['text'][0]
        
    context = response['context']

    return json.dumps({'status': 'OK', 'msg': msg})


app.run()