from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import render_template
from markupsafe import escape
import pyodbc 

cnxn = pyodbc.connect(r'Driver=SQL Server;Server=DESKTOP-R8VD1QD\SQLEXPRESS;Database=mortorhub;Trusted_Connection=yes;')


app = Flask(__name__,  static_url_path='',
                    static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM categories;")
    categories = cur.fetchall()
    cur.execute("SELECT * FROM cars;")
    cars = cur.fetchone()
    cur.execute("SELECT * FROM cars WHERE cars.range = 1;")
    lowbudget = cur.fetchall()
    cur.execute("SELECT * FROM cars WHERE cars.range = 2;")
    midrange = cur.fetchall()
    cur.execute("SELECT * FROM cars WHERE cars.range = 3;")
    highend = cur.fetchall()
    cur.execute("SELECT * FROM cars WHERE cars.range = 4;")
    category = cur.fetchall()
    cur.execute("SELECT * FROM cars WHERE cars.range = 5;")
    insta = cur.fetchall()
    cur.execute("SELECT * FROM cars WHERE cars.range = 6;")
    indexpic = cur.fetchall()
    cur.execute("SELECT * FROM cars WHERE cars.carid = 138;")
    deal = cur.fetchall()
    cursor = cnxn.cursor()
    return render_template('layout.html', categories=categories, cars=cars, lowbudget=lowbudget, midrange=midrange, highend=highend, category=category, insta=insta, indexpic=indexpic, deal=deal)


@app.route('/<id>' ,  methods=['GET', 'POST'])
def cate1(id):
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM cars;")
    cars = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.execute(
        "SELECT * from categories join cars on (categories.categoryid = cars.categoryid)  WHERE categories.categoryid = " + id)
    catetype = cur.fetchall()
    cur.connection.commit()
    cur.close()
    return render_template('shop.html', cars=cars, categories=categories, catetype=catetype)

@app.route('/range/<range>' ,  methods=['GET', 'POST'])
def range(range):
    cur = cnxn.cursor()
    cur.execute("SELECT * FROM cars;")
    cars = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.execute(
        "SELECT * from cars WHERE cars.range = " + range)
    ranges = cur.fetchall()
    cur.connection.commit()
    cur.close()
    return render_template('range.html', cars=cars, categories=categories, ranges=ranges)
