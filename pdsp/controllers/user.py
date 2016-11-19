from extension import mysql, login_manager, mail
from flask import *
from flask.ext.login import login_user, logout_user, UserMixin, login_required, current_user
from flask.ext.mail import Message
import hashlib
import os

user = Blueprint('user', __name__, template_folder='views')

@user.route('/user', methods=['GET','POST'])
def user_signup_route():
    if current_user.is_authenticated==True:
        return redirect('/')
    if request.method=="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        company = request.form.get("company")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM User WHERE username="%s"'%username)
        if cur.fetchone()!=None:
            flash("Account already exist!", "error")
            return render_template("login.html", type="signup")
        if password!=password2:
            flash("Passwords not the same!", "error")
            return render_template("login.html", type="signup")
        passwordEn = hashlib.md5(password).hexdigest()
        cur.execute('INSERT INTO User VALUES("%s","%s","%s","%s","%s")'%(username,passwordEn,email,phone,company))
        mysql.connection.commit()
        user = User(username, passwordEn)
        login_user(user)
        msg = Message("Siemens Production Document System",recipients=[email],html=render_template("email_signup.html",username=username,host=request.host))
        mail.send(msg)
        return redirect('/')
    else:
        return render_template("login.html", type="signup")

@user.route('/user/login', methods=['GET','POST'])
def user_login_route():
    if current_user.is_authenticated==True:
        return redirect('/')
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        next = request.form.get("next")
        cur = mysql.connection.cursor()
        cur.execute('SELECT password FROM User WHERE username="%s"'%username)
        passwordDB = cur.fetchone()
        if passwordDB==None:
            flash("Account not exist!", "error")
            return render_template("login.html", type="login", next=next)
        elif passwordDB[0] == hashlib.md5(password).hexdigest():
            user = User(username, passwordDB[0])
            login_user(user)
            if next=="None":
                return redirect('/')
            else:
                return redirect(next)
        else:
            flash("Password incorrect!", "error")
            return render_template("login.html", type="login", next=next)
    else:
        next = request.args.get("next")
        if next!=None:
            flash("Please login to access.", "error")
        return render_template("login.html", type="login", next=next)

@user.route('/user/logout')
@login_required
def user_logout_route():
    logout_user()
    return redirect('/')

@user.route('/user/forgot', methods=['POST'])
def user_forgot_route():
    username = request.form.get("username")
    cur = mysql.connection.cursor()
    cur.execute('SELECT email FROM User WHERE username="%s"'%username)
    email = cur.fetchone()
    if email==None:
        flash("Account not exist!", "error")
        return render_template("login.html", type="login")
    token = hashlib.md5(username).hexdigest()
    msg = Message("Siemens SPDS: Reset your password!",recipients=[email[0]],html=render_template("email_forgot.html",username=username,token=token,host=request.host))
    mail.send(msg)
    flash("An email was sent to the address you provided during registration process. Please follow the link to reset password!", "success")
    return render_template("login.html", type="login")

@user.route('/user/reset', methods=['GET','POST'])
def user_reset_route():
    username = request.args.get("username")
    token = request.args.get("token")
    if token == hashlib.md5(username).hexdigest():
        if request.method=="POST":
            password = request.form.get("password")
            password2 = request.form.get("password2")
            if password!=password2:
                flash("Passwords not the same!", "error")
                return render_template("login.html", type="reset")
            cur = mysql.connection.cursor()
            passwordEn = hashlib.md5(password).hexdigest()
            cur.execute('UPDATE User SET password="%s" WHERE username="%s"'%(passwordEn,username))
            mysql.connection.commit()
            flash("Successfully change password!", "success")
            return render_template("login.html", type="login")
        else:
            return render_template("login.html", type="reset")
    else:
        return render_template("404.html"),404

@user.route('/user/edit', methods=['GET','POST'])
@login_required
def user_edit_route():
    if request.method=="POST":
        username = current_user.id
        submit = request.form.get("submit")
        if submit=="Save":
            email = request.form.get("email")
            phone = request.form.get("phone")
            company = request.form.get("company")
            cur = mysql.connection.cursor()
            cur.execute('UPDATE User SET email="%s", phone="%s", company="%s" WHERE username="%s"'%(email,phone,company,username))
            mysql.connection.commit()
            cur.execute('SELECT phone, company, email FROM User WHERE username="%s"'%username)
            user = cur.fetchone()
            flash("Successfully save!", "success")
            return render_template("login.html", type="edit", user = user)
        elif submit=="Change Password":
            passwordOld = request.form.get("passwordOld")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            cur = mysql.connection.cursor()
            cur.execute('SELECT phone, company, email FROM User WHERE username="%s"'%username)
            user = cur.fetchone()
            cur.execute('SELECT password FROM User WHERE username="%s"'%username)
            passwordDB = cur.fetchone()
            if passwordDB[0] != hashlib.md5(passwordOld).hexdigest():
                flash("Old password incorrect!", "error")
                return render_template("login.html", type="edit", user = user)
            if password!=password2:
                flash("Passwords not the same!", "error")
                return render_template("login.html", type="edit", user = user)
            passwordEn = hashlib.md5(password).hexdigest()
            cur.execute('UPDATE User SET password="%s" WHERE username="%s"'%(passwordEn,username))
            mysql.connection.commit()
            flash("Successfully change password!", "success")
            return render_template("login.html", type="edit", user = user)
        elif submit=="Delete":
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM User WHERE username="%s"'%username)
            mysql.connection.commit()
            logout_user()
            return redirect('/')
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT phone, company, email FROM User WHERE username="%s"'%current_user.id)
        user = cur.fetchone()
        return render_template("login.html", type="edit", user = user)

class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return User(user_id,"123")
