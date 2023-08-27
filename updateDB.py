import sqlite3
from readDB import readMovies, searchMoviesByName
from flask import Flask
conn = sqlite3.connect('movies.sqlite')
cur = conn.cursor()


# with open("./createTable.sql") as file:
#     sql_script = file.read()

# cur.executescript(sql_script)

app = Flask("__main__")
@app.route("/")
def index():
    return "congratulations, it's a web app!"
def addMovie(name, year, genre, director):
    if(name and year and genre and director):
        cur.execute("INSERT INTO moviesMain (name, year, genre, director) VALUES (?, ?, ?, ?)", (name, year, genre, director))
    else: return "missing data"

# addMovie('Tár', 2023, "psychological drama", "Todd Field")
# readMovies(cur)    
print(searchMoviesByName(cur, "Creed III"))
# app.run(host="127.0.0.1", port=8080, debug=True)


cur.close()
conn.close()