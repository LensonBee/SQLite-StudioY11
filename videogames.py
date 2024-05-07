# SQLite cars database thing

import sqlite3

DATABASE = 'videogames.db'


def print_all_games():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        # SQLite Query
        sql = "SELECT * FROM game;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print results

    for car in results:
        print(f"{game}")


if __name__ == "__main__":
    print_all_games()
