
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
        return redirect(url_for('fixer'))
  
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
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('proposal'))
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
    customerinfo=db.child()
    return redirect(url_for('proposal'))
  return render_template('choosen.html')

@app.route('/fixer', methods=['GET','POST'])
def fixer():
  consumers=db.child('Users').get().val()
  return render_template("fixer.html", consumers=consumers)

@app.route('/offer/<ida>', methods=['GET','POST'])
def offer(ida):
  print(ida)
  if request.method=="POST":
    offer = request.form['offer1']
    updated2={"offer":offer}
    UID=login_session['user']['localId']
    db.child("Users").child(ida).update(updated2)
    return render_template('offer.html', i=ida)
  else:
    return render_template('offer.html', i=ida)

@app.route('/proposal', methods=['GET','POST'])
def proposal():
  UID=login_session['user']['localId']
  customer=db.child("Users").child(UID).get().val()

  if 'offer' in customer.keys():
    prop=customer['offer']
    
    return render_template('date.html', p=prop)
  return render_template('date.html')


@app.route('/decision', methods=['GET','POST'])
def decision():
  if request.method == 'POST':
    ans=request.form['opt']
    if ans=='reject':
      UID=login_session['user']['localId']
      db.child("Users").child(UID).child('offer').remove()
      return render_template('reject.html')

    else:
      UID=login_session['user']['localId']
      db.child("Users").child(UID).child('offer').remove()
      return render_template('accept.html')
  else:
    return render_template('date.html')



@app.route('/signout', methods=['GET', 'POST'])
def signout():
  login_session['user']=None
  auth.current_user=None

  return redirect(url_for('signin'))










    
    
 

  return render_template("date.html")
if __name__ == '__main__':   
    app.run(debug=True)   
