
from flask import Flask, render_template, request,url_for,redirect
from flask import session as login_session
import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyDtEzuOwbFDNemnguiwxTLprxVh8hFbykc",
  'authDomain': "auth-lab-5fcd3.firebaseapp.com",
  'projectId': "auth-lab-5fcd3",
  'storageBucket': "auth-lab-5fcd3.appspot.com",
  'messagingSenderId': "105981837328",
  'appId': "1:105981837328:web:e4f6a7bc3342288d314a95",
  "databaseURL":"https://auth-lab-5fcd3-default-rtdb.europe-west1.firebasedatabase.app/"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
db =firebase.database()
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/signup', methods=['GET', 'POST'])
def signup():

  return render_template('welcome.html')
