import sqlite3
def readMovies(cur):
    movies_data = cur.execute("SELECT * FROM moviesMain ORDER BY rowid")
    for row in movies_data:
        print(row)
def searchMoviesByName(cur, name):
    movies_data = cur.execute("SELECT * FROM moviesMain WHERE name=?", (name,))
    return movies_data