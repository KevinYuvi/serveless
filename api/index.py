from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola desde Flask serverless"

# Vercel usará directamente este WSGI app
# y NO necesita un 'handler' explícito si el archivo se llama index.py
wsgi_app = app.wsgi_app
