#Assorted functions to do with the registration process.

TOTALGENRES = 3

import data

def selectedGender(userData):
    o = {'male':'', 'female':'', 'other':''}
    o[userData['gender']] = 'selected'
    return o

def selectedGenres(userData):
    genres = {'genre1':userData['genre1'], 'genre2':userData['genre2'], 'genre3':userData['genre3']}
    for key, item in genres.items():
        if item == 'on':
            genres[key] = 'checked'
        else:
            genres[key] = ''
    return genres

def validationPassword(password):
    return any(char.isdigit() for char in password) and any(char.isupper() for char in password)

def userAdd(userData):
    d = {'uname':userData['uname'],
        'password':userData['password'],
        'name':"{0} {1}".format(userData['fname'], userData['lname']),
        'postcode':userData['postcode'],
        'birthdate':userData['birthdate'],
        'gender':userData['gender'],
        'genres':{}}
    for i in range(1, TOTALGENRES + 1):
        d['genres']['genre' + str(i)] = True if (userData['genre' + str(i)] == 'checked') else False
    return data.accountsUpdate(d)
