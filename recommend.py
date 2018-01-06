#These functions handle the film recommendations.

import data

def genreCount(user): #Determine how preferred each genre is for a particular user.
    userData = data.accountsRecall(user) #Get this user's data from the database.
    films = data.filmsRecall() #Get the films database. A bad idea if there were lots of films, but fine for our 12.
    genrePoints = {'genre1':0, 'genre2':0, 'genre3':0} #Create the dict we'll use to assign points to genres. Flaw: not extensible.
    for film in userData['lastviewed'].split(','): #Iterates over the last ten films viewed by the user.
        if film == 'DEFAULT':
            break #Don't waste time if we've already reached the "end" of the list.
        else:
            for g in films[film]['genres'].split(','): #This gets us that film's genre(s) as a list and iterates over that list.
                genrePoints[g] += 1
    for g in userData['genres'].split(','): #Now also take into account the genres the user chose when they first registered.
        genrePoints[g] += 1
    return genrePoints

def filmSort(user, genrePoints): #Sort films based on the genre scoring.
    userData = data.accountsRecall(user)
    films = data.filmsRecall() #Get the list of films from the database.
    genreSort = sorted(genrePoints, key=genrePoints.get)[::-1] #Sort the genres based on their weightings. Greatest first.
    filmsSort = []
    for genre in genreSort: #Iterate over the genres and films and add them in order of preferred genre.
        for film, i in films.items():
            if not film == 'DEFAULT':
                print(i)
                if genre in i['genres'] and not film in filmsSort and not film in userData['lastviewed']:
                    filmsSort.append(film) #Films in the last 10 viewed are ignored for now.
    for genre in genreSort: #The same thing, but this time with only the last 10 viewed, adding them to the end of the list.
        for film, i in films.items():
            if not film == 'DEFAULT':
                if genre in i['genres'] and not film in filmsSort and film in userData['lastviewed']:
                    filmsSort.append(film)
    return filmsSort

def filmSelect(films, amount): #Shorten a list of films and include the rest of their data.
    filmDb = data.filmsRecall()
    filmsFinal = {}
    for film in films[0:amount]:
        filmsFinal[film] = filmDb[film]
    return filmsFinal
