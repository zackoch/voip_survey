import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dotenv
from secrets import token_hex

dotenv.load_dotenv()

path = token_hex(6)
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from voip_survey import routes