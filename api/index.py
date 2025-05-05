from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola desde Flask adaptado a Vercel 🚀"

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
