# SQLite cars database thing

import sqlite3

DATABASE = 'videogames.db'


def print_all_games():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # SQLite Query
    sql = "SELECT * FROM game;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    print("Name                          Genre")
    for game in results:
        print(f"{game[1]:<30}{game[2]:<8}")


if __name__ == "__main__":
    print_all_games()
