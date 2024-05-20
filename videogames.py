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



# main code
while True:
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        2. Search by name
        3. Search by studio
        4. Add element (not done)
        7. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        search_game()
    elif user_input == "3":
        search_studio()
    elif user_input == "7":
        break
    else:
        print("\nThat was not an option")

# I'm racist™
