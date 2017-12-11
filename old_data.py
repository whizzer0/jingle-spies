#import sqlite3

#Run this only on initial creation or if it all goes horribly wrong.
#def databaseSetup():
#    acc = sqlite3.connect("accounts.db")
#    accCommand = '''
#                CREATE TABLE account (
#                account_id INTEGER PRIMARY KEY,
#                name VARCHAR(50),
#                postcode VARCHAR(8),
#                birthdate DATE,
#                gender CHAR(1),
#                genre_action CHAR(1),
#                genre_comedy CHAR(1),
#                genre_romance CHAR(1),
#                film_0 VARCHAR(2),
#                film_1 VARCHAR(2),
#                film_2 VARCHAR(2),
#                film_3 VARCHAR(2),
#                film_4 VARCHAR(2),
#                film_5 VARCHAR(2),
#                film_6 VARCHAR(2),
#                film_7 VARCHAR(2),
#                film_8 VARCHAR(2),
#                film_9 VARCHAR(2)'''