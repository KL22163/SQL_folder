"""A code which allows you to search for pokemon by their type and name
By Katrina Lai 2024"""
#Selecting the SQL database
import sqlite3
DATABASE = "poke_type.db"

def pokemon_type():
#Showing the type and correseponding number
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM Typings"
        cursor.execute(sql)
        results = cursor.fetchall()
        for types in results:
            print(types[0], types[1])
#Asking what pokemon types to sort by, search by type
def pokemon_of_type():
    print("Please input the number corresponding to the pokemon type, if there is no second type leave Type 2 blank.")
    while True:
        try:
            type_1 = input("Type 1: ")
            if 0 < int(type_1) < 19:
                break
        except:
            print("That is an invalid input, please try again.")
    while True:
        try:
            type_2 = input("Type 2: ")
            if type_2 == "":
                break
            elif int(type_2) > 0 and int(type_2) < 19:
                break
        except:
            print("That is an invalid input, please try again.")
#If input is only one type:
    if type_2 == "":
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Pokemons.poke_name FROM Pokemons WHERE Pokemons.type_1 = ? OR Pokemons.type_2 = ?;"
            cursor.execute(sql,(type_1, type_1))
            results = cursor.fetchall()
            for pokemons in results:
                print(pokemons[0])
#If input has two types:
    else:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Pokemons.poke_name FROM Pokemons WHERE Pokemons.type_1 = ? AND Pokemons.type_2 = ? OR Pokemons.type_1 = ? AND Pokemons.type_2 = ?;"
            cursor.execute(sql,(type_1, type_2, type_2, type_1))
            #Print results- Search by type
            results = cursor.fetchall()
            for pokemons in results:
                print(pokemons[0])
            if not results:
                print("There aren't any Pokemon with this type combination.")

#Printing a list of pokemon, ids and names
def list_of_pokemon():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT id, poke_name FROM Pokemons"
        cursor.execute(sql)
        results = cursor.fetchall()
        for names in results:
            print(names[0], names[1])
#Asking which pokemon to search by, search by name
def type_of_pokemon():
        print("Please input the number corresponding to the pokemon name.")
        while True:
            try:
                poke_id = input("Pokemon Number: ")
                if 0 < int(poke_id) < 152:
                    break
            except:
                print("Invalid input, please try again.")
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = f"SELECT poke_name FROM Pokemons WHERE Pokemons.id == {poke_id};"
            cursor.execute(sql)
            results = cursor.fetchall()
            for name in results:
                print(name[0] + ":")
            cursor = db.cursor()
            sql = f"SELECT type_name FROM Typings JOIN Pokemons ON Pokemons.type_1 = Typings.id WHERE Pokemons.id == {poke_id};"
            cursor.execute(sql)
#Print results- search by name
        results = cursor.fetchall()
        for type_names in results:
            print(type_names[0])
        cursor = db.cursor()
        sql = f"SELECT type_name FROM Typings JOIN Pokemons ON Pokemons.type_2 = Typings.id WHERE Pokemons.id == {poke_id};"
        cursor.execute(sql)
#Print results- search by name
        results = cursor.fetchall()
        for type_names in results:
            print(type_names[0])

#Selection menu
while True:
    user_input = input("""What would you like to do?
    1 - Search By Type
    2 - Search By Name
    3 - Exit
    """)
    if user_input == "1":
        pokemon_type()
        pokemon_of_type()
    elif user_input == "2":
        list_of_pokemon()
        type_of_pokemon()
    elif user_input == "3":
        print("Thanks for playing! :D")
        break
    else:
        print("Invalid input, please try again.")