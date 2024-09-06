from flask import render_template,request, redirect, url_for, session
from . import app
import sqlite3
from . import functions
from datetime import datetime

@app.route('/')
def home():
    estados = functions.get_estados()
    disciplinas = functions.get_disciplinas()
    return render_template('home.html', estados=estados,disciplinas=disciplinas)

@app.route('/insert_user', methods=['POST'])
def insert_user():
    data = request.form.to_dict()
    dateinsert = datetime.now()
    data['datestart'] = dateinsert
    session['participante_id'] = functions.save_participante(data)
    return redirect(url_for('form', page=0))

@app.route('/form/<int:page>', methods=['GET', 'POST'])
def form(page):
    participante_id = session.get('participante_id')
    if not participante_id:
        return redirect(url_for('home'))    
    preguntas, opciones = functions.get_preguntas(page,numpreguntas=3)

    if request.method == 'POST':
        respuestas = request.form.to_dict()
        print(f'ID del participante: {participante_id}')
        print(respuestas)
        functions.save_respuestas(respuestas,participante_id)
        return redirect(url_for('form', page=page + 1))

    return render_template('form.html', preguntas=preguntas, page=page, opciones=opciones)