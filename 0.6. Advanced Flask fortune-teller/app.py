from flask import Flask,render_template
import random
fortunelist=["youll get accepted to the MIT","Lill will win the worldcup","SARI KHAMIS will get beat up by hasan","Amir will win watan in a fist fight",]
app = Flask(__name__,template_folder='templates')

@app.route('/home')
def home ():
	return (render_template('lill.html'))

@app.route('/fortune')
def fortune():
	rand=random.choice(fortunelist)
	return(render_template('fortune.html',rand=rand))


if __name__ == '__main__':   
    app.run(debug=True)   