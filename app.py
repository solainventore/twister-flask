# flask app to use local .sqlite3 database
# for login,register, and user profile with profile image in base64

import sqlite3
import os
import base64
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# create flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"