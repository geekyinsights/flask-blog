#imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

#configuration
DATABASE = 'blog.db'

app = Flask(_name_)

app.config.from_object(_name_)
#pulls in app configuration by looking for UPPERCASE variables
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
if _name_ == '_main_':
    app.run(debug=True)
