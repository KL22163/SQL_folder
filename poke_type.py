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
    type_1 = input("Type 1: ")
    type_2 = input("Type 2: ")
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
    name = input("Pokemon Name: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = f"SELECT type_1, type_2 FROM Pokemons WHERE poke_name = {name}"
        cursor.execute(sql)
        #Print results- search by name
        results = cursor.fetchall()
        for names in results:
            print(names[0])

while True:
#Selection menu
    user_input = input("""What would you like to do?
    1 - Search By Type
    2 - Search By Name
    3 - Guessing game
    4 - Exit
    """)
    if user_input == "1":
        pokemon_type()
        pokemon_of_type()
    elif user_input == "2":
        list_of_pokemon()
        type_of_pokemon()
    elif user_input == "4":
        print("Thanks for playing! :D")
        break