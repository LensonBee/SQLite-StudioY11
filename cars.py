# SQLite cars database thing

import sqlite3

DATABASE = 'cars.db'


def print_all_cars():
    speed = input("What speed: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        # SQLite Query
        sql = "SELECT * FROM car WHERE top_speed > ?;"
        cursor.execute(sql, (speed,))
        results = cursor.fetchall()
        # print results

    for car in results:
        print(f"Car: {car[1]} Top Speed: {car[2]}")


if __name__ == "__main__":
    print_all_cars()
