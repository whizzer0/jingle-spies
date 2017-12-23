#These functions access and modify the database of accounts and films.

import configparser

def accountsUpdate(d):
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

def filmsUpdate(d):
    db = configparser.ConfigParser()
    db.read('films.ini')
    db[d['id']] = {'Title':d['title'],
                   'Genres':d['genres']}
    with open('films.ini', 'a') as dbFile:
        db.write(dbFile)
        
def accountsRecall(account):
    db = configparser.ConfigParser()
    db.read('accounts.ini')
    return db[account]
    
def filmsRecall():
    db = configparser.ConfigParser()
    db.read('films.ini')
    return db
