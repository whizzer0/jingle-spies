#This is essentially the webserver backend - it serves pages that are requested by the user, and carries input between the pages.

from flask import Flask, render_template, request
import join, recommend, data

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

def recommendDisplayable():
    filmsFive = recommend.filmSelect(recommend.filmSort(user, recommend.genreCount(user)), 5)
    filmTitles = []
    filmIDs = []
    for filmTitle, film in filmsFive.items():
        filmTitles.append(film['title'])
        filmIDs.append(str(film)[10:-1])
    return {'filmsFive':filmsFive, 'filmTitles':filmTitles, 'filmIDs':filmIDs}

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
    if join.validationPassword(userData['password']) and not userData['uname'] in data.accountsRecall():
        join.userAdd(userData)
        user = userData['uname']
        return render_template('register-success.html', userData=userData)
    else:
        return render_template('register.html', userData=userData, error=True)

@app.route('/home', methods=['GET'])
def pageGetHome():
    filmVars = recommendDisplayable()
    return render_template('home.html', films=filmVars['filmsFive'], filmTitles=filmVars['filmTitles'], filmIDs=filmVars['filmIDs'])
    
@app.route('/home', methods=['POST'])
def pagePostHome():
    button = request.form.to_dict()
    b = list(button.keys())[0]
    if b[-6:] == '_watch':
        u = data.accountsRecall(user)
        films = u['lastviewed'].split(',')
        filmsFinal = list(films)
        for index, film in enumerate(films):
            if film == 'DEFAULT':
                filmsFinal[index] = b[:-6]
                break
            if index == 9:
                filmsFinal[0] = b[:-6]
                break
        filmsFinal = ','.join(filmsFinal)
        u['uname'] = user
        data.accountsUpdate(u, filmsFinal)
    filmVars = recommendDisplayable()
    return render_template('home-post.html', films=filmVars['filmsFive'], filmTitles=filmVars['filmTitles'], filmIDs=filmVars['filmIDs'])

if __name__ == '__main__':
	app.run()
