#These functions handle the film recommendations.

import data

def count(user):
    userData = data.accountsRecall(user) #Get this user's data from the database.
    films = data.filmsRecall() #Get the films database. A bad idea if there were lots of films, but fine for our 12.
    genrePoints = {'genre1':0, 'genre2':0, 'genre3':0} #Create the dict we'll use to assign points to genres. Flaw: not extensible.
    for film in userData['lastviewed']: #Iterates over the last ten films viewed by the user.
        if film == 'Default':
            break #Don't waste time if we've already reached the "end" of the list.
        else:
            for g in films[film]['genres'].split(','): #This gets us that film's genre(s) as a list and iterates over that list.
                genrePoints[g] += 1
