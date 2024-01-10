from flask import Blueprint, request, render_template, session, redirect, url_for
import pymysql
from database import db

restaurant_app = Blueprint('restaurant_app', __name__, template_folder='templates')

@restaurant_app.route('/mon-restaurant', methods=['GET', 'POST'])
def mon_restaurant():

    db_config = db.db_config

    db_conn = pymysql.connect(**db_config)
    cursor = db_conn.cursor()

    cursor.execute('SELECT nom, telephone, addresse FROM restaurants where user_id = %s', (session['id']))
    findRestaurant = cursor.fetchone()

    if request.method == 'POST':
        nom = request.form.get('nom')
        telephone = request.form.get('telephone')
        addresse = request.form.get('addresse')

        if not findRestaurant:
            cursor.execute('insert into restaurants(nom, telephone, addresse, user_id) values(%s, %s, %s, %s)', (nom, telephone, addresse, session['id']))
        else:
            cursor.execute('update restaurants set nom=%s, telephone = %s, addresse = %s where user_id=%s', (nom, telephone, addresse, session['id']))

        db_conn.commit()
        return redirect(url_for('restaurant_app.mon_restaurant'))

    return render_template("mon_restaurant.html", restaurant = findRestaurant)