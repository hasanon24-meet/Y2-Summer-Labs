
from flask import Flask, render_template, request,url_for,redirect
from flask import session as login_session
import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyDtEzuOwbFDNemnguiwxTLprxVh8hFbykc",
  'authDomain': "auth-lab-5fcd3.firebaseapp.com",
  'projectId': "auth-lab-5fcd3",
  'storageBucket': "auth-lab-5fcd3.appspot.com",
  'messagingSenderId': "105981837328",
  'appId': "1:63095860232:web:875054c9c12db7bb41f5bd",
  "databaseURL":"https://myproject-f96f7-default-rtdb.europe-west1.firebasedatabase.app/"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
db =firebase.database()
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    consumer = request.form['consumer']
    name = request.form['name1']
    user={"email":email,"consumer":consumer,"name":name}
    try:
      login_session['user'] = auth.create_user_with_email_and_password(email, password)
      UID =login_session['user']['localId']
      db.child("Users").child(UID).set(user)
      if consumer=='service':
        return redirect(url_for('choosen'))

      else:
        return render_template('welcome.html')
  
    except Exception as e:
      error = "Authentication failed"
      print(e)
    return render_template('welcome.html')
  else:
    return render_template("welcome.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    consumer = request.form['consumer']

    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      return render_template('signin.html')
    except:
      error = "Authentication failed"
      print(error)
  return render_template("signin.html")

@app.route('/choosen', methods=['GET', 'POST'])
def choosen():
  if request.method=="POST":
    sengine = request.form['engine']
    ref = request.form['kind']
    updatedinfo={"engine":sengine,"kind":ref}
    UID=login_session['user']['localId']
    db.child("Users").child(UID).update(updatedinfo)
    return redirect(url_for('date'))
  return render_template('choosen.html')



@app.route('/date', methods=['GET','POST'])
def date():
  return render_template("date.html")
if __name__ == '__main__':   
    app.run(debug=True)   
