from flask import Flask
from .config import Config  # Aseg�rate de que la importaci�n sea correcta

app = Flask(__name__)
app.config.from_object(Config)  # Carga la configuraci�n desde el objeto Config

from . import routes