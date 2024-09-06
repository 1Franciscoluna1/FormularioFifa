import sqlite3

def create_tables():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    
    # Crear tabla de participantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            sexo_id INTERGER NOT NULL,
            estado_id INTERGER NOT NULL,
            disciplina_id INTERGER NOT NULL,
            encuesta_id INTERGER NOT NULL,
            datestart TIMESTAMP NOT NULL,
            FOREIGN KEY (estado_id) REFERENCES estados (id),
            FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id)
                   
        )
    ''')
    
    # Crear tabla de respuestas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participante_id INTEGER,
            pregunta_id INTEGER,
            opcion_id INTEGER,
            FOREIGN KEY (participante_id) REFERENCES participantes (id),
            FOREIGN KEY (opcion_id) REFERENCES opciones (id)
        )
    ''')

    #Crear tabla de sexos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sexos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion INTEGER
        )
        insert into sexos (descripcion)
    values ('Mujer'), ('Hombre')
                   
    ''')


    
    conn.commit()
    conn.close()

# Llama a esta función al inicio de tu aplicación
create_tables()