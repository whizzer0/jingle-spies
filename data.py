import configparser

def databaseStoreAccount(d):
    db = configparser.ConfigParser()
    db.read('accounts.ini')
    films = ','.join(['0' for i in range(10)])
    db[d['id']] = {'Name':d['name'],
                     'Postcode':d['postcode'],
                     'Birthdate':d['birthdate'],
                     'Gender':d['gender'],
                     'SelectedGenres':','.join(genres),
                     'LastViewed':films}
    with open('accounts.ini', 'ab') as dbFile:
        db.write(dbFile)

def databaseStoreFilm(d):
    db = configparser.ConfigParser()
    db.read('films.ini')
    db[d['id']] = {'Title':d['title'],
                   'Genres':d['genres']}
    with open('films.ini', 'ab') as dbFile:
        db.write(dbFile)