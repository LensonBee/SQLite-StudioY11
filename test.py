# SQLite cars database thing

import sqlite3

DATABASE = 'cars.db'

with sqlite3.connect(DATABASE) as db:
    db = sqlite3.connect('cars.db')
    cursor = db.cursor()
    # SQLite Query
    sql = "SELECT * FROM car ORDER BY top_speed DESC;"

    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    for car in results:
        print(car)
