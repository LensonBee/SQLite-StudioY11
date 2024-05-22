# SQLite videogames database thing
# imports
import sqlite3

# constants and variables
DATABASE = 'videogames.db'


# functions
def print_all_games():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results
    print("\nName                                    Genre", end='')
    print("               Rating              Studio")
    for game in results:
        print(f"{game[0]:<40}{game[1]:<20}{game[2]:<20}{game[3]}")
    # loop finished here
    db.close()


def print_all_studios():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM studio;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results
    print("\nID                  Name")
    for studio in results:
        print(f"{studio[0]:<20}{studio[1]}")
    # loop finished here
    db.close()


def search_game():
    try:
        search = str(input("Search for a game below: \n"))
        search = '%' + search + '%'
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id WHERE name LIKE ?;"
        cursor.execute(sql, (search,))
        results = cursor.fetchall()
        # loop through all results
        print("\nName                                    Genre", end='')
        print("               Rating              Studio")
        for game in results:
            print(f"{game[0]:<40}{game[1]:<20}{game[2]:<20}{game[3]}")
        # loop finished here
    except:
        print("\nInvalid query")
    db.close()


def search_studio():
    search = str(input("Search for a studio below: \n"))
    search = '%' + search + '%'
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name,genre,metacritic_rating,studio_name FROM studio INNER JOIN game ON studio.studio_id=game.studio_id WHERE studio_name LIKE ?;"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    # loop through all results
    print("\nName                                    Genre", end='')
    print("               Rating              Studio")
    for game in results:
        print(f"{game[0]:<40}{game[1]:<20}{game[2]:<20}{game[3]}")
    # loop finished here
    db.close()


def add_element():
    # ask user for which table
    user_input = input("""
        Choose a table to add to.
        1. Games
        2. Studios
        """)
    if user_input == "1":
        print("not added yet")
    elif user_input == "2":
        add_studio()
    else:
        print("\nThat was not an option")


def add_studio():
    # ask user for new studio name
    print("\nEnter new studio below")
    new_name = input()
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # insert new studio
    sql = "INSERT INTO studio (studio_name) VALUES (?);"
    cursor.execute(sql, (new_name,))
    db.commit()  # commit changes to table
    print("Studio added")
    db.close()


def delete_element():
    # ask user for which table
    user_input = input("""
        Choose a table to delete something from.
        1. Games
        2. Studios
        """)
    if user_input == "1":
        print("not added yet")
    elif user_input == "2":
        delete_studio()
    else:
        print("\nThat was not an option")


def delete_studio():
    # ask user for studio name to remove
    print("\nEnter studio to delete below")
    delete_name = input()
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # delete studio
    sql = ";"
    cursor.execute(sql, (delete_name,))
    db.commit()  # commit changes to table
    print("Studio added")
    db.close()


# main code
while True:
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        2. Print all studios
        3. Search by game
        4. Search by studio
        5. Add element (work in progress)
        6. Delete element (work in progress)
        9. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        print_all_studios()
    elif user_input == "3":
        search_game()
    elif user_input == "4":
        search_studio()
    elif user_input == "5":
        add_element()
    elif user_input == "9":
        break
    else:
        print("\nThat was not an option")

# Quantum Tunneling™
