from flask import Flask

app = Flask(__name__) #to define the app

from app import views1
from app import gvoice