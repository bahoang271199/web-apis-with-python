# dictionary-api-python-flask/models/dbHandler.py
import sqlite3 as SQL
def match_exact (word: str) -> list:

# Establish connection to the dictionary database
    db = SQL.connect( "data/dictionary.db" )
    sql_query = "SELECT * from entries WHERE word=?"
#  Query the database for exact matches
    match = db.execute(sql_query, (word,)).fetchall()
# Clone the connection to the database
    db.close()
# Return the results
    return match

def match_like (word: str) -> list:

# Establish connection to the dictionary database
    db = SQL.connect( "data/dictionary.db" )
# Query the database for exact matches
    sql_query = "SELECT * from entries WHERE word LIKE ?"
    match = db.execute(sql_query, ( "%" + word + "%" ,)).fetchall()
# Clone the connection to the database
    db.close()
# Return the res
    return match

    