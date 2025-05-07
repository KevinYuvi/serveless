from flask import Flask
from vercel_wsgi import handle_request  # Importa el adaptador correcto

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola desde Flask en Vercel 🚀'

# Este es el handler real que Vercel espera
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
