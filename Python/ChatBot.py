#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json, watson_developer_cloud

class pessoa:
    def __init__(self,no_matricula):
        self.no_matricula = no_matricula
        self.nome = ''


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

@app.route('/')
def chat():
    response = conversation.message(
        workspace_id=workspace_id,
        input={
            'text': user_input
        }
    )
    global usuario
    global user_context
    user_context = response
    usuario = pessoa(0)
    return render_template('ChatBot.html')


@app.route('/receiver', methods=['POST'])
def usermsg():
    
    global usuario
    data = request.get_json()
    user_input = data['msg']

    recebe_nomatricula(user_input)

    msg = comunica_Watson(user_input)
    
    return json.dumps({'status': 'OK', 'msg': msg})


def comunica_Watson(user_input):
    global user_context

    response = conversation.message(
        workspace_id=workspace_id,
        input={
            'text': user_input
        },
        context = user_context['context']
    )

    user_context = response

    print(response)

    return response['output']['text'][0]

def recebe_nomatricula(user_input):

    global usuario
    
    if((verifica_no(user_input)) & (len(user_input) == 10)):
        usuario.no_matricula = int(user_input)
        return True
    else:
        return False

def verifica_no(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

app.run()