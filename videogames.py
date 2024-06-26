# SQLite videogames database thing
# imports
import sqlite3
from getpass import getpass


class color:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'


# constants and variables
DATABASE = 'videogames.db'


# functions
def print_all_games():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sort = input("""
        What do you want to sort by?
        1. Alphabetical order
        2. Genre
        3. Studio
        4. Metacritic score
        5. Exit
        """)
    if sort == "1":
        sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id ORDER BY name ASC;"
    elif sort == "2":
        sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id ORDER BY genre ASC;"
    elif sort == "3":
        sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id ORDER by studio_name ASC;"
    elif sort == "4":
        sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id ORDER by metacritic_rating DESC;"
    elif sort == "5":
        return
    else:
        print(color.red + "That was not an option" + color.end)
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results
    print(color.cyan + "\nName                                    Genre", end='')
    print("               Rating              Studio")
    for game in results:
        print(f"{game[0]:<40}{game[1]:<20}{game[2]:<20}{game[3]}")
    print(color.end)
    # loop finished here
    db.close()


def print_all_studios():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM studio ORDER BY studio_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all results
    print(color.cyan + "\nID                  Name")
    for studio in results:
        print(f"{studio[0]:<20}{studio[1]}")
    print(color.end)
    # loop finished here
    db.close()


def search():
    # ask user for which table
    user_input = input("""
        What do you want to search by?
        1. Game name
        2. Studio name
        3. Exit
        """)
    if user_input == "1":
        search_game()
    elif user_input == "2":
        search_studio()
    elif user_input == "3":
        return
    else:
        print(color.red + "\nThat was not an option" + color.end)


def search_game():
    search = str(input("Search for a game below: \n"))
    search = '%' + search + '%'
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name, genre, metacritic_rating, studio_name FROM game INNER JOIN studio ON game.studio_id=studio.studio_id WHERE name LIKE ?;"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    # check if there are no results
    if results == "[]":
        print(color.red + "No results found" + color.end)
    # loop through all results
    print(color.cyan + "\nName                                    Genre", end='')
    print("               Rating              Studio")
    for game in results:
        print(f"{game[0]:<40}{game[1]:<20}{game[2]:<20}{game[3]}")
    print(color.end)
    # loop finished here
    db.close()


def search_studio():
    search = str(input("Search for a studio below: \n"))
    search = '%' + search + '%'
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT name,genre,metacritic_rating,studio_name FROM studio INNER JOIN game ON studio.studio_id=game.studio_id WHERE studio_name LIKE ?;"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    # check if there are no results
    if results == "[]":
        print(color.red + "No results found" + color.end)
    # loop through all results
    print(color.cyan + "\nName                                    Genre", end='')
    print("               Rating              Studio")
    for game in results:
        print(f"{game[0]:<40}{game[1]:<20}{game[2]:<20}{game[3]}")
    print(color.end)
    # loop finished here
    db.close()


def add_element():
    # ask user for which table
    user_input = input("""
        Choose a table to add to.
        1. Games
        2. Studios
        3. Exit
        """)
    if user_input == "1":
        add_game()
    elif user_input == "2":
        add_studio()
    elif user_input == "3":
        return
    else:
        print(color.red + "\nThat was not an option" + color.end)


def add_game():
    # ask user details of new game
    name = input("Enter the name: ")
    genre = input("Enter the genre: ")
    while True:
        rating = int(input("Enter the metacritic rating: "))
        if rating > 100 or rating < 1:
            print(color.red + "Enter a number between 1 and 100")
        else:
            break
    studio_name = input("Enter the studio: ")
    studio_name = '%' + studio_name + '%'
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # find studio
    sql = "SELECT studio_id FROM studio WHERE studio_name LIKE ?;"
    cursor.execute(sql, (studio_name,))
    result = cursor.fetchone()
    if result:
        studio_id = result[0]
    else:
        # if studio does not exist
        add_studio = input(color.yellow + "Studio not found, do you want to add it? (yes / no)\n" + color.end)
        if add_studio.lower() == "yes":
            # insert new studio
            studio_name = studio_name.replace("%", "")
            sql = "INSERT INTO studio (studio_name) VALUES (?);"
            cursor.execute(sql, (studio_name,))
            db.commit()
            # retrieve id of new studio
            sql = "SELECT studio_id FROM studio WHERE studio_name LIKE ?;"
            cursor.execute(sql, (studio_name,))
            result = cursor.fetchone()
            studio_id = result[0]
        else:
            print(color.red + "Game not added" + color.end)
            db.close()
            return  # exit the function
    # insert new game
    sql = "INSERT INTO game (name, genre, metacritic_rating, studio_id) VALUES (?,?,?,?);"
    cursor.execute(sql, (name, genre, rating, studio_id))
    db.commit()  # commit changes to table
    print(color.green + "Game added" + color.end)
    db.close()


def add_studio():
    # ask user for new studio name
    new_name = input("\nEnter new studio below: \n")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # insert new studio
    sql = "INSERT INTO studio (studio_name) VALUES (?);"
    cursor.execute(sql, (new_name,))
    db.commit()  # commit changes to table
    print(color.green + "Studio added" + color.end)
    db.close()


def delete_element():
    # ask user for which table
    user_input = input("""
        Choose a table to delete something from.
        1. Games
        2. Studios
        3. Exit
        """)
    if user_input == "1":
        delete_game()
    elif user_input == "2":
        delete_studio()
    elif user_input == "3":
        return
    else:
        print(color.red + "\nThat was not an option" + color.end)


def delete_game():
    # ask user for game name to remove
    delete_name = input("\nEnter game to delete below: \n")
    if delete_name != "":  # check if delete query is blank
        delete_name = '%' + delete_name + '%'
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # ask user if they're sure
        confirmation = input(color.red + "Are you sure you want to permanently delete this? (yes / no) " + color.end)
        if confirmation == "yes":
            pass
        else:
            print(color.yellow + "Function stopped" + color.end)
            return
        # delete game
        sql = "DELETE FROM game WHERE name LIKE ?;"
        cursor.execute(sql, (delete_name,))
        db.commit()  # commit changes to table
        print(color.green + "Game deleted" + color.end)
        db.close()
    else:
        print(color.red + "Game not found" + color.end)


def delete_studio():
    # ask user for studio name to remove
    delete_name = input("\nEnter studio to delete below: \n")
    if delete_name != "":  # check if delete query is blank
        delete_name = '%' + delete_name + '%'
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # ask user if they're sure
        confirmation = input(color.red + "Are you sure you want to permanently delete this? (yes / no) " + color.end)
        if confirmation == "yes":
            pass
        else:
            print(color.yellow + "Function stopped" + color.end)
            return
        # delete studio
        sql = "DELETE FROM studio WHERE studio_name LIKE ?;"
        cursor.execute(sql, (delete_name,))
        db.commit()  # commit changes to table
        print(color.green + "Studio deleted" + color.end)
        db.close()
    else:
        print(color.red + "Studio not found" + color.end)


# main code
while True:
    account = input(
        """
        What account are you using?
        1. Editor
        2. Viewer
        3. Exit
        """)
    if account == "1":
        password = getpass("Password: ")
        if password == "1234":  # password
            account = "editor"
            print(color.green + "Access granted" + color.end)
            break
        else:
            print(color.red + "Access denied" + color.end)
    elif account == "2":
        account = "viewer"
        print(color.green + "Viewer access granted" + color.end)
        break
    elif account == "3":
        break
    else:
        print(color.red + "\nThat was not an option" + color.end)

while account == "editor":  # Admin/editor
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        2. Print all studios
        3. Search
        4. Add element
        5. Delete element
        8. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        print_all_studios()
    elif user_input == "3":
        search()
    elif user_input == "4":
        add_element()
    elif user_input == "5":
        delete_element()
    elif user_input == "8":
        break
    else:
        print(color.red + "\nThat was not an option" + color.end)

while account == "viewer":  # Viewer/guest
    user_input = input(
        """
        What would you like to do.
        1. Print all games
        2. Print all studios
        3. Search
        8. Exit
        """)
    if user_input == "1":
        print_all_games()
    elif user_input == "2":
        print_all_studios()
    elif user_input == "3":
        search()
    elif user_input == "8":
        break
    else:
        print(color.red + "\nThat was not an option" + color.end)

# I'm severely schizophrenic and refer to the voices in my head as chat™
