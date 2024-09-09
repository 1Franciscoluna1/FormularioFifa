from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Estado, Disciplina, Participante, Sexo, Pregunta, Opcion, Respuesta
import os
from dotenv import load_dotenv

load_dotenv()

# Obtener variables de entorno
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

# Construir URL especial de SQLAlchemy
dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

# Crear motor SQLAlchemy
engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)

# Crear un sessionmaker para manejar las sesiones
Session = sessionmaker(bind=engine)

def get_estados():
    session = Session()
    estados = session.query(Estado).all()
    session.close()
    return estados

def get_disciplinas():
    session = Session()
    disciplinas = session.query(Disciplina).filter_by(status=1).order_by(Disciplina.nombre.asc()).all()
    print(disciplinas)
    session.close()
    return disciplinas

def save_participante(data):
    session = Session()
    participante = Participante(
        firstname=data['firstname'],
        lastname=data['lastname'],
        sexo_id=data['sexo'],
        estado_id=data['estado'],
        disciplina_id=data['disciplina'],
        encuesta_id=data['encuesta'],
        datestart=data['datestart']
    )
    session.add(participante)
    session.commit()
    session.refresh(participante)
    participante_id = participante.id
    session.close()
    return participante_id

def get_preguntas(page, numpreguntas):
    session = Session()
    preguntas = session.query(Pregunta).offset(page * numpreguntas).limit(numpreguntas).all()
    
    opciones = {}
    for pregunta in preguntas:
        opc = session.query(Opcion).filter_by(pregunta_id=pregunta.id).all()
        opciones[pregunta.id] = opc
    
    session.close()
    return preguntas, opciones

def save_respuestas(respuestas, participante_id):
    session = Session()
    for pregunta_id, respuesta in respuestas.items():
        respuesta_obj = Respuesta(
            participante_id=participante_id,
            pregunta_id=pregunta_id,
            opcion_id=respuesta
        )
        session.add(respuesta_obj)
    session.commit()
    session.close()

get_disciplinas()