from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
    "apiKey" : "AIzaSyC2vm5Bta4G1jpKVZRUxD4ZdTqU-Q7yuC0",
    "authDomain" : "proof-of-concept-70d46.firebaseapp.com",
    "projectId" : "proof-of-concept-70d46",
    "storageBucket" : "proof-of-concept-70d46.appspot.com",
    "messagingSenderId" : "859196437655",
    "appId": "1:859196437655:web:738f70b3fb835b5ede65d2",
    "measurementId" : "G-27HV52T6BY",
    "databaseURL": "https://proof-of-concept-70d46-default-rtdb.firebaseio.com/"
  }

firebase = pyrebase.initialize_app(config)

db= firebase.database()