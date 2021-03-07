from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import render_template
from flask_mysqldb import MySQL
from markupsafe import escape

app = Flask(__name__,  static_url_path='',
                    static_folder='static', template_folder='templates')
                    
# local
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Uv1ndu2006'
app.config['MYSQL_DB'] = 'mortorhub'

# production
# application.config['MYSQL_HOST'] = 'database-1.c5qdsuoy5mft.ap-south-1.rds.amazonaws.com'
# application.config['MYSQL_USER'] = 'admin'
# application.config['MYSQL_PASSWORD'] = ''
# application.config['MYSQL_DB'] = 'home_delivary'


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mortorhub.categories;")
    categories = cur.fetchall()
    cur.execute("SELECT * FROM mortorhub.cars;")
    cars = cur.fetchall()
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
    cur.close()
    return render_template('index.html', categories=categories, cars=cars, lowbudget=lowbudget, midrange=midrange, highend=highend, category=category, insta=insta, indexpic=indexpic, deal=deal)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/shopping-cart')
def cart():
    return render_template('shopping-cart.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


# @app.route('/cate/<id>',  methods=['GET', 'POST'])
# def categories(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM cars")
#     cars = cur.fetchall()
#     cur.execute("SELECT * FROM categories")
#     categories = cur.fetchall()
#     cur.execute(
#         "SELECT * from categories join cars on (categories.categoryid = cars.categoryid) WHERE categories.categoryid =" + id)
#     catetype = cur.fetchall()
#     cur.connection.commit()
#     cur.close()
#     return render_template('shop.html', cars=cars, categories=categories, catetype=catetype)

@app.route('/<id>' ,  methods=['GET', 'POST'])
def cate1(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cars")
    cars = cur.fetchall()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()
    cur.execute(
        "SELECT * from categories join cars on (categories.categoryid = cars.categoryid) WHERE categories.categoryid =" + id)
    catetype = cur.fetchall()
    cur.connection.commit()
    cur.close()
    return render_template('shop.html', cars=cars, categories=categories, catetype=catetype)
    