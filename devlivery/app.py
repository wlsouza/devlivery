from flask import Flask
from devlivery.ext import site

def create_app():
    app = Flask(__name__)
    site.init_app(app)
    return app
