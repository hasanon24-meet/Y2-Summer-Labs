
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
  "databaseURL":""
  }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      login_session['quotes']= []
      return render_template('home.html')
    except:
      error = "Authentication failed"
      print(error)
  return render_template("signin.html")
   
@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method=='GET':
    return render_template("home.html")
  else:
    quote = request.form['quote']
    login_session['quotes'].append(quote)
    login_session.modified = True

    print('x')
    print(login_session['quotes'])

    return render_template("thanks.html")


@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      login_session['user'] = auth.create_user_with_email_and_password(email, password)

      login_session['quotes']= []
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      print(error)
    return render_template('signin.html')
  else:
    return render_template("signup.html")


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
  return render_template("thanks.html")


@app.route('/display', methods=['GET', 'POST'])
def display():
  return render_template("display.html",quotesl = login_session['quotes'])


@app.route('/signout', methods=['GET', 'POST'])
def signout():
  login_session['user']=None
  auth.current_user=None
  print("signed out")

  return redirect(url_for('signin'))



if __name__ == '__main__':   
    app.run(debug=True)   
