from flask import Flask  # Importa la herramienta para hacer webs

app = Flask(__name__)  # Crea una aplicación web

@app.route('/')  # Cuando alguien visite la página principal
def hola_mundo():
    return "¡Hola Ivan, esta cosa ya funciona, esto lo escribí en Spyder a las 5:50, ya me quiero ir. Llevo casi 30 minutos peleando porque no sé como subir desde mi compu local (spyder) a GitHub!"  # Esto es lo que verán

if __name__ == '__main__':
    app.run()  # Inicia el servidor