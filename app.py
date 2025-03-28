from flask import Flask  # Importa la herramienta para hacer webs

app = Flask(__name__)  # Crea una aplicación web

@app.route('/')  # Cuando alguien visite la página principal
def hola_mundo():
    return "¡Mi primer sitio web!"  # Esto es lo que verán

if __name__ == '__main__':
    app.run()  # Inicia el servidor