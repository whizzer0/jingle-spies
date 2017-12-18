#Account creation

from data import *

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
