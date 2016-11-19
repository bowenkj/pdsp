# -*- coding: utf-8 -*-
from flask import Flask, render_template, session
import controllers
from extension import mysql, login_manager, mail
from datetime import timedelta
import os

app = Flask(__name__, template_folder='views')

app.register_blueprint(controllers.product)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.user)
app.register_blueprint(controllers.doc)
app.register_blueprint(controllers.inprogress)

app.config['MYSQL_DB'] = 'spds'
app.config['MYSQL_USER'] = 'siemens'
app.config['MYSQL_PASSWORD'] = 'JIsiemens2016'
app.config['MYSQL_CHARSET'] = 'utf8'
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = "Siemens_SPDS@163.com"
app.config['MAIL_USERNAME'] = "Siemens_SPDS"
app.config['MAIL_PASSWORD'] = "JIsiemens163" #mail auth pwd
#mail login pwd: JIsiemens2016
app.config['SECRET_KEY'] = "SECRET"
mysql.init_app(app)
login_manager.init_app(app)
mail.init_app(app)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)

# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True, )
