#This is essentially the webserver backend - it serves pages that are requested by the user, and carries input between the pages.

from flask import Flask, render_template, request
import join, recommend

user = 'whizzer0'
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
    global user
    userData = request.form.to_dict()
    userData['genre1'] = userData.get('genre1', False)
    userData['genre2'] = userData.get('genre2', False)
    userData['genre3'] = userData.get('genre3', False)
    userData.update(join.selectedGender(userData))
    userData.update(join.selectedGenres(userData))
    if join.validationPassword(userData['password']):
        join.userAdd(userData)
        user = userData['uname']
        return render_template('register-success.html', userData=userData)
    else:
        return render_template('register.html', userData=userData, error=True)

@app.route('/home', methods=['GET'])
def pageGetHome():
    filmsFive = recommend.filmSelect(recommend.filmSort(user, recommend.genreCount(user)), 5)
    filmTitles = []
    filmIDs = []
    for filmTitle, film in filmsFive.items():
        filmTitles.append(film['title'])
        filmIDs.append(str(film)[10:-1])
    return render_template('home.html', films=filmsFive, filmTitles=filmTitles, filmIDs=filmIDs)

if __name__ == '__main__':
	app.run()
