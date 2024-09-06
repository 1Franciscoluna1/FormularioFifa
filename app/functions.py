import sqlite3

# Conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('Database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_estados():
    # Conectar a la base de datos
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    
    # Obtener todos los estados
    cursor.execute('SELECT id, nombre FROM estados')
    estados = cursor.fetchall()
    
    # Cerrar la conexión
    conn.close()
    
    return estados

def get_disciplinas():
    # Conectar a la base de datos
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    
    # Obtener todos los estados
    cursor.execute('SELECT * FROM disciplinas WHERE status = 1 ORDER BY nombre ASC')
    estados = cursor.fetchall()
    
    # Cerrar la conexión
    conn.close()
    
    return estados

def save_participante(data):
    conn = get_db_connection()
    cur = conn.execute('INSERT INTO participantes (firstname, lastname, sexo_id, estado_id, disciplina_id, encuesta_id, datestart) VALUES (?,?,?,?,?,?,?)', (data['firstname'], data['lastname'], data['sexo'], data['estado'], data['disciplina'], data['encuesta'], data['datestart']))
    conn.commit()
    # Obtener el id del participante recién insertado
    participante_id = cur.lastrowid
    conn.close()
    return participante_id


def get_preguntas(page,numpreguntas):
    conn = get_db_connection()
    preguntas = conn.execute(f'SELECT * FROM preguntas LIMIT '+str(numpreguntas)+' OFFSET ?', (page * numpreguntas,)).fetchall()
    
    opciones = {}
    for pregunta in preguntas:
        opc = conn.execute('SELECT * FROM opciones WHERE pregunta_id = ?', (pregunta['id'],)).fetchall()
        opciones[pregunta['id']] = opc
    conn.close()
    return preguntas,opciones

def save_respuestas(respuestas,participante_id):
    conn = get_db_connection()
    for pregunta_id, respuesta in respuestas.items():
        conn.execute('INSERT INTO respuestas (participante_id, pregunta_id, opcion_id) VALUES (?, ?, ?)', (participante_id,pregunta_id, respuesta))
    conn.commit()
    conn.close()