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

@app.route('/')
def chat():
    return render_template('ChatBot.html')


@app.route('/receiver', methods=['POST'])
def usermsg():
    data = request.get_json()
    user_input = data['msg']
    print(user_input)

    response = conversation.message(
        workspace_id=workspace_id,
        input={
            'text': user_input
        }
    )

    # If an intent was detected, print it to the console.
    if response['intents']:
        intent = response['intents'][0]['intent']
        if intent == 'saudação':
            msg = 'Olá, em que posso ajudar?'
        elif intent == 'despedida':
            msg = 'Adeus, espero que a sua dúvida tenha sido respondida'

    return json.dumps({'status': 'OK', 'msg': msg})


app.run()