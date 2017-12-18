#This is essentially the webserver backend - it serves pages that are requested by the user, and carries input between the pages.

from flask import Flask, render_template, request
import join

userDataBlank = {'uname':"",
                'password':"",
                'name':("", ""),
                'postcode':"",
                'birthdate':"",
                'gender':"",
                'genre1':True,
                'genre2':False,
                'genre3':False}

app = Flask(__name__)
app.debug = True

@app.route('/register', methods=['GET'])
def pageGetRegister():
	return render_template('register.html', userData=userDataBlank, error=False)

@app.route('/register', methods=['POST'])
def pagePostRegister():
    userData = request.form.to_dict()
    userData['genre1'] = userData.get('genre1', False)
    userData['genre2'] = userData.get('genre2', False)
    userData['genre3'] = userData.get('genre3', False)
    userData.update(join.selectedGender(userData))
    userData.update(join.selectedGenres(userData))
    if join.validationPassword(userData['password']):
        #join.userAdd(userData)
        return render_template('register-success.html', userData=userData)
    else:
        return render_template('register.html', userData=userData, error=True)
	
if __name__ == '__main__':
	app.run()
