from flask import Flask, request, render_template, redirect, url_for, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from controller.login import login_app
from controller.index import index_app
from controller.restaurant import restaurant_app

app = Flask(__name__)
app.register_blueprint(index_app)
app.register_blueprint(login_app)
app.register_blueprint(restaurant_app)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.run()
