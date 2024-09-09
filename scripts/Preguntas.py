import sqlite3
import json

# Conectar a la base de datos
# conn = sqlite3.connect('Database.db')
# cursor = conn.cursor()

# # Crear las tablas
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS preguntas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     texto TEXT NOT NULL,
#     clase INTEGER NOT NULL
# );
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS opciones (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     pregunta_id INTEGER,
#     peso INTEGER NOT NULL,
#     texto TEXT NOT NULL,
#     FOREIGN KEY (pregunta_id) REFERENCES preguntas(id)
# );
# ''')

# JSON de entrada
data = '''[
    {
        "pregunta": "Me veo más como un perdedor que como un ganador durante las competencias.",
        "clase": 1,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me enojo y frustro en los partidos.",
        "clase": 2,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me distraigo y pierdo la concentración en las competencias.",
        "clase": 3,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    { 
        "pregunta": "Antes de competir me veo rindiendo perfectamente.",
        "clase": 4,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Estoy altamente motivado para jugar lo mejor que pueda.",
        "clase": 5,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo mantener una corriente mi energía positiva durante las competencias.",
        "clase": 6,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Soy un pensador positivo durante las competencias.",
        "clase": 7,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Creo en mí mismo como deportista.",
        "clase": 1,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me pongo nervioso o tengo miedo en las competencias.",
        "clase": 2,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Parece que mi cabeza se acelera a 100 km/h por hora durante los momentos críticos de las competencias.",
        "clase": 3,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Practico mentalmente mis habilidades físicas.",
        "clase": 4,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Las metas que me he propuesto como deportista me hacen trabajar mucho.",
        "clase": 5,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo disfrutar las competencias aunque tenga muchos problemas difíciles.",
        "clase": 6,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me digo cosas negativas durante las competencias.",
        "clase": 7,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Pierdo la confianza rápidamente.",
        "clase": 1,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Los errores durante los partidos, me llevan a sentir y pensar negativamente.",
        "clase": 2,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo borrar emociones que interfieren y volverme a concentrar durante las competencias.",
        "clase": 3,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "La visualización de mi deporte me es fácil.",
        "clase": 4,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "No me tienen que empujar para jugar o entrenar duro. Yo me estimulo solo.",
        "clase": 5,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Tiendo a sentirme aplastado emocionalmente cuando las cosas se vuelven en mi contra.",
        "clase": 6,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Yo doy un 100% de esfuerzo cuando me desempeño en mi deporte sin importarme nada.",
        "clase": 7,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo rendir al 100% de mi talento y habilidad.",
        "clase": 1,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Mis músculos se tensan durante las competencias.",
        "clase": 2,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me desconcentro durante las competencias.",
        "clase": 3,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Yo me visualizo saliendo de situaciones difíciles antes de las competencias.",
        "clase": 4,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Estoy dispuesto a dar todo lo necesario para llegar a mi máximo potencial como deportista.",
        "clase": 5,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Entreno con alta actitud positiva.",
        "clase": 6,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo cambiar de estados emocionales (sentimientos) negativos a positivos por medio del control mental.",
        "clase": 7,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Soy un competidor con fortaleza mental.",
        "clase": 1,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Sentimientos incontrolables como el miedo, rivales tramposos y malos hábitos me molestan.",
        "clase": 2,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Mientras me desempeño en mi deporte me encuentro pensando en errores pasados u oportunidades perdidas.",
        "clase": 3,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Uso imágenes mientras me desempeño que me ayudan a rendir mejor.",
        "clase": 4,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me aburro y agoto.",
        "clase": 5,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me lleno de sensaciones de desafío y me inspiro en situaciones difíciles.",
        "clase": 6,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Mis entrenadores dirían que tengo una buena actitud.",
        "clase": 7,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Yo transmito la imagen de un atleta con confianza en sí mismo.",
        "clase": 1,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo mantenerme calmado durante las competencias cuando estoy confundido por problemas.",
        "clase": 2,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Mi concentración se rompe fácilmente.",
        "clase": 3,
        "opciones": [
            {
                "peso": "1",
                "texto": "Casi Siempre"
            },
            {
                "peso": "2",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "4",
                "texto": "Pocas Veces"
            },
            {
                "peso": "5",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Cuando me visualizo jugando puedo ver y sentir las cosas vívidamente.",
        "clase": 4,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Me despierto por la mañana y estoy realmente excitado por practicar mi deporte y entrenar.",
        "clase": 5,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Practicar mi deporte me da una sensación genuina de alegría y plenitud.",
        "clase": 6,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    },
    {
        "pregunta": "Puedo transformar una crisis en oportunidad.",
        "clase": 7,
        "opciones": [
            {
                "peso": "5",
                "texto": "Casi Siempre"
            },
            {
                "peso": "4",
                "texto": "A menudo"
            },
            {
                "peso": "3",
                "texto": "A veces"
            },
            {
                "peso": "2",
                "texto": "Pocas Veces"
            },
            {
                "peso": "1",
                "texto": "Casi Nunca"
            }
        ]
    }
]'''

# Cargar el JSON
json_data = json.loads(data)
current_pregunta_id = 1
# Insertar preguntas y opciones
for pregunta in json_data:
    print('INSERT INTO preguntas (texto, clase) VALUES (?, ?)', (pregunta['pregunta'], pregunta['clase']))
    pregunta_id = current_pregunta_id  # Obtener el ID de la última pregunta insertada

    for opcion in pregunta['opciones']:
        print('INSERT INTO opciones (pregunta_id, peso, texto) VALUES (?, ?, ?)', (pregunta_id, opcion['peso'], opcion['texto']))

    current_pregunta_id += 1
# Guardar los cambios y cerrar la conexión
# conn.commit()
# conn.close()