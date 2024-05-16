# SQLite videogames database thing
# imports
import sqlite3

# constants and variables
DATABASE = 'videogames.db'


# functions
def print_all_games():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM game;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results
    print("Name                               Genre", end='')
    print("               Rating         Studio_id")
    for game in results:
        print(f"{game[1]:<35}{game[2]:<20}{game[3]:<15}{game[4]}")
    # loop finished here
    db.close()


def custom_query():
    print("Enter custom query below", end="")
    try:
        userquery = str(input(": \n"))
    except ValueError:
        print("Invalid query")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(userquery)
    results = cursor.fetchall()
    # loop through all results
    print("Name                               Genre", end='')
    print("               Rating         Studio_id")
    for game in results:
        print(f"{game[1]:<35}{game[2]:<20}{game[3]:<15}{game[4]}")
    # loop finished here
    db.close()


# main code
while True:
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        2. Custom query
        7. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        custom_query()
    elif user_input == "7":
        break
    else:
        print("That was not an option")
