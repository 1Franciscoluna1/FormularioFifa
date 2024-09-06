import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('Database.db')

# Crear un cursor
cursor = conn.cursor()

# Crear la tabla 'estados'
cursor.execute('''
CREATE TABLE IF NOT EXISTS estados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
''')

# Lista de estados de la República Mexicana
estados_mexico = [
    'Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche',
    'Chiapas', 'Chihuahua', 'Coahuila', 'Colima', 'Durango', 'Guanajuato',
    'Guerrero', 'Hidalgo', 'Jalisco', 'Estado de México', 'Michoacán',
    'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro',
    'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco',
    'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas'
]

# Insertar los estados en la tabla
for estado in estados_mexico:
    cursor.execute('INSERT INTO estados (nombre) VALUES (?)', (estado,))

# Guardar los cambios
conn.commit()

# Consultar y mostrar los datos
cursor.execute('SELECT * FROM estados')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()