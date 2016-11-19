# Siemens SPDS

Siemens Production Document System

## Setup: Do the following once

### installation

install python

install flask

install mysql

install virtualenvironment

pull source files

create venv: virtualenvironment venv

### init mysql:

mysql -uroot

mysql> create database spds;

mysql> create user siemens;

mysql> grant all on spds.* to 'siemens'@'localhost' identified by 'JIsiemens2016';

mysql> alter table spds default character set utf8 collate utf8_bin;

mysql -usiemens spds -pJIsiemens2016 < sql/tbl_create.sql

### init flask:

. venv/bin/activate

pip install flask,mysql,mysqldb,flask_mail,flask_login

## Setup: Do the following each time you run the app

cd {}\pdsp
start venv: . venv/bin/activate

to run locally: python app.py

to run on server: gunicorn -b 0.0.0.0:80 -w 4 -D app:app (kill previous one first)
