from flask import Flask, render_template
from flask.ext.mysqldb import MySQL
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
mysql = MySQL()

login_manager = LoginManager()
login_manager.login_view = "user.user_login_route"

mail = Mail()
