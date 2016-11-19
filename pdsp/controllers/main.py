from flask import *
import os
from extension import mysql
from flask.ext.login import login_required, current_user

main = Blueprint('main', __name__, template_folder='views')

@main.route('/', methods=['GET','POST'])
def main_route():
	if current_user.is_authenticated==True:
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM Product WHERE creator="%s" ORDER BY productid DESC;'%current_user.id)
		allproducts = cur.fetchall()
		if request.args.get("search") is None:
			search = request.form.get("product")
		else:
			search = request.args.get("search")
		if search is not None:
			cur.execute('SELECT * FROM Product WHERE name LIKE "%%%s%%" AND creator="%s" ORDER BY productid DESC;'%(search,current_user.id))
			products = cur.fetchall()
			return render_template("index.html", allproducts=allproducts, products=products, search=True, next=search, len=len(products))
		else:
			return render_template("index.html", allproducts=allproducts, search=False)
	else:
		return render_template("index.html")

@main.route('/create', methods=['POST'])
@login_required
def create_route():
    name = request.form.get("name")
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO Product (name,creator) VALUES ("%s","%s");'%(name,current_user.id))
    mysql.connection.commit()
    cur.execute('SELECT productid FROM Product ORDER BY productid DESC;')
    productid = cur.fetchone()[0]
    # print productid
    os.mkdir('static/uploads/%s'%productid)
    os.mkdir('static/uploads/%s/spec'%productid)
    os.mkdir('static/uploads/%s/vgbmkb'%productid)
    os.mkdir('static/uploads/%s/program'%productid)
    os.mkdir('static/uploads/%s/wi'%productid)
    os.mkdir('static/uploads/%s/refdoc'%productid)
    # cur.execute('INSERT INTO ProductAccess (productid,username) VALUES ("%s","%s");'%(productid,current_user.id))
    # mysql.connection.commit()
    return redirect('/product?id=%s&next='%productid)