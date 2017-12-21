#These functions access and modify the database of accounts and films.

import configparser

def databaseAccountsUpdate(d):
    db = configparser.ConfigParser()
    db.read('accounts.ini')
    films = ','.join(['Default' for i in range(10)])
    genres = []
    for genre, value in d['genres'].items():
        if value:
            genres.append(genre)
    db[d['uname']] = {'Password':d['password'], #Told you it was horrendously insecure.
                     'Name':d['name'],
                     'Postcode':d['postcode'],
                     'Birthdate':d['birthdate'],
                     'Gender':d['gender'],
                     'SelectedGenres':','.join(genres),
                     'LastViewed':films}
    with open('accounts.ini', 'a') as dbFile:
        db.write(dbFile)
    return d['uname']

def databaseFilmsUpdate(d):
    db = configparser.ConfigParser()
    db.read('films.ini')
    db[d['id']] = {'Title':d['title'],
                   'Genres':d['genres']}
    with open('films.ini', 'a') as dbFile:
        db.write(dbFile)
        
def databaseRecall(account, database = 'accounts.ini'):
    db = configparser.ConfigParser
    db.read(database)
    return db[account]
