from flask import Flask, request, json
from flask_marshmallow import Marshmallow


app = Flask(__name__, template_folder="./../templates", static_folder="./../static")
ma = Marshmallow(app=app)

from src.routes import *
