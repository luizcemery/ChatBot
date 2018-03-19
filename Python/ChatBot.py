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
    global user_context
    data = request.get_json()
    user_input = data['msg']

    entidade = ''
    entidade_valor = ''
    if(user_context['entities']):
        entidade = user_context['entities'][0]['entity']
        entidade_valor =  user_context['entities'][0]['value']
    
    if(entidade == 'inconsistencia'):
        if(recebe_nomatricula(user_input)):
            msg = verifica_cadastro()
            comunica_Watson('')
        else:
            msg = 'Por favor reenvie a sua matrícula apenas com os números'
    else:
        msg = comunica_Watson(user_input)
    
    
    return json.dumps({'status': 'OK', 'msg': msg})

def verifica_cadastro():

    global usuario
    flag = False

    if(flag):
        print('Cadastro existente.')
    else:
        return 'Não foi identificado nenhum cadastro no minhaUFMG associado ao número de matrícula ' + str(usuario.no_matricula) + '. Para realizar o cadastro basta acessar o <a href="https://sistemas.ufmg.br/nip" target="_blank">link</a> e informar o seu CPF e senha provisória cadastrada para ter acesso à sua folha de NIPs'

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