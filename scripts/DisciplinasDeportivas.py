import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('Database.db')

# Crear un cursor
cursor = conn.cursor()

# Crear una tabla para las disciplinas deportivas con la columna 'status'
cursor.execute('''
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    status INTEGER NOT NULL
)
''')

# Lista de disciplinas deportivas y su estado (1 para activo, 0 para inactivo)
disciplinas_deportivas = [
    ("Fútbol", 1),
    ("Baloncesto", 1),
    ("Tenis", 1),
    ("Natación", 1),
    ("Atletismo", 1),
    ("Ciclismo", 1),
    ("Voleibol", 1),
    ("Golf", 1),
    ("Rugby", 1),
    ("Boxeo", 1),
    ("Béisbol", 1),
    ("Hockey", 1),
    ("Esquí", 1),
    ("Surf", 1),
    ("Gimnasia", 1)
]

# Insertar disciplinas en la tabla
for disciplina, status in disciplinas_deportivas:
    cursor.execute('INSERT INTO disciplinas (nombre, status) VALUES (?, ?)', (disciplina, status))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()