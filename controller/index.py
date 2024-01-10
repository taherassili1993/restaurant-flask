from flask import Blueprint, request, render_template, session, redirect, url_for
import pymysql
from database import db

index_app = Blueprint('index_app', __name__, template_folder='templates')

@index_app.route('/')
def welcome():
    db_config = db.db_config

    db_conn = pymysql.connect(**db_config)
    cursor = db_conn.cursor()

    sql = db.sql
 
    cursor.execute(sql)

    return render_template("index.html")