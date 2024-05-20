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
    print("Name                                    Genre", end='')
    print("               Rating              Studio_id")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<20}{game[3]:<20}{game[4]}")
    # loop finished here
    db.close()


def search_game():
    search = str(input("Search for a game below: \n"))
    search = '%' + search + '%'
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM game WHERE name LIKE ?;"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    # loop through all results
    print("Name                                    Genre", end='')
    print("               Rating              Studio_id")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<20}{game[3]:<20}{game[4]}")
    # loop finished here
    db.close()


def search_studio():
    search = str(input("Search for a studio below: \n"))
    search = '%' + search + '%'
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM studio WHERE studio_name LIKE ?;"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    # loop through all results
    print("Name                                    Genre", end='')
    print("               Rating              Studio_id")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<20}{game[3]:<20}{game[4]}")
    # loop finished here
    db.close()


def custom_query():
    print("Enter custom query below", end="")
    try:
        userquery = str(input(": \n"))
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute(userquery)
        results = cursor.fetchall()
        # loop through all results
        print("Name                                    Genre", end='')
        print("               Rating              Studio_id")
        for game in results:
            print(f"{game[1]:<40}{game[2]:<20}{game[3]:<20}{game[4]}")
    except:
        print("Invalid query")
        return
        custom_query()
    # loop finished here
    db.close()


def add_element():
    print("Enter new element below (INSERT INTO game ())", end="")
    try:
        element = str(input(": \n"))
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute(userquery)
        results = cursor.fetchall()
        # loop through all results
        print("Name                                    Genre", end='')
        print("               Rating              Studio_id")
        for game in results:
            print(f"{game[1]:<40}{game[2]:<20}{game[3]:<20}{game[4]}")
    except:
        print("Invalid query")
        return
        custom_query()
    # loop finished here
    db.close()


# main code
while True:
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        2. Search by name
        3. Search by studio
        4. Custom query
        5. Add element (not done)
        7. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        search_game()
    elif user_input == "3":
        search_studio()
    elif user_input == "4":
        custom_query()
    elif user_input == "7":
        break
    else:
        print("That was not an option")
