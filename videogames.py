# SQLite videogames database thing
# imports
import sqlite3

# constants and variables
DATABASE = 'videogames.db'


# functions
def print_all_games():
    # print all games nicely
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM game;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results
    print("Name                          Genre               Rating         Studio_id")
    for game in results:
        print(f"{game[1]:<30}{game[2]:<20}{game[3]:<20}{game[4]:<15}")
    # loop finished here
    db.close()


# main code
while True:
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        7. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        pass
    elif user_input == "7":
        break
    else:
        print("That was not an option")
