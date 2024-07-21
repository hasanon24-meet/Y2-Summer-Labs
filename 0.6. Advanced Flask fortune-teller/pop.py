from flask import Flask,render_template,request,redirect,url_for
import random
app = Flask(__name__,template_folder='templates')

fortunelist=["youll get accepted to the MIT","Lill will win the worldcup","SARI KHAMIS will get beat up by hasan","Amir will win watan in a fist fight","Shalev moves to Kazakhstan","lill will become cs lead","hasan stays th best in the world","hasan will do his bonus","Ibrahem becomes the president of the USA","SARI KHAMIS will become a y1 lead","meet wil add another meet value"]
@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
	    return render_template('lill.html')
	else:
	    birth = request.form['birth']	   
	    return redirect(url_for('fortune',
	        Birthmonth = birth))
	return render_template('lill.html')

@app.route('/fortune/<Birthmonth>')
def fortune(Birthmonth):

	numbers=len(Birthmonth)
	if numbers<10:
		return(render_template('fortune.html',fortunemsg=fortunelist[len(Birthmonth)]))
	else:
		return render_template('finish.html')


if __name__ == '__main__':   
    app.run(debug=True)   