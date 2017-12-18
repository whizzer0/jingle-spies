from flask import Flask, render_template, request
import join

app = Flask(__name__)
app.debug = True

@app.route('/register', methods=['GET'])
def pageGetRegister():
	return render_template('register.html')

@app.route('/results', methods=['POST'])
def pagePostRegisterSuccess():
    userData = {'name':request.form['name'], 'home':request.form['home'], 'dob':request.form['dob'], 'sex':request.form['sex'], 'genre1':request.form['genre1'], 'genre2':request.form['genre2'], 'genre3':request.form['genre3']}
    #join.userAdd(userData)
    return render_template('register-success.html', username=userData['name'])
	
if __name__ == '__main__':
	app.run()
