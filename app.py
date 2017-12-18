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
    print(userData)
    userData['genre1'] = userData.get('genre1', False)
    userData['genre2'] = userData.get('genre2', False)
    userData['genre3'] = userData.get('genre3', False)
    print(userData)
    userData.update(join.selectedGender(userData))
    userData.update(join.selectedGenres(userData))
    print(userData)
    #if join.passValidate(userData['pass']):
        #join.userAdd(userData)
    if False:
        return render_template('register-success.html', userData=userData)
    else:
        return render_template('register.html', userData=userData, error=True)
	
if __name__ == '__main__':
	app.run()
