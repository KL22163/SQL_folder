#Selecting the SQL database
import sqlite3
DATABASE = "poke_type.db"

#Asking what pokemon types to sort by, search by type
def print_all_pokemon():
    type_1 = input("Type 1: ")
    type_2 = input("Type 2: ")
    if type_2 == "":
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Pokemons.poke_name FROM Pokemons WHERE Pokemons.type_1 = ? OR Pokemons.type_2 = ?;"
            cursor.execute(sql,(type_1, type_1))
            results = cursor.fetchall()
            for pokemons in results:
                print(pokemons[0])
    else:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Pokemons.poke_name FROM Pokemons WHERE Pokemons.type_1 = ? AND Pokemons.type_2 = ? OR Pokemons.type_1 = ? AND Pokemons.type_2 = ?;"
            cursor.execute(sql,(type_1, type_2, type_2, type_1))
            results = cursor.fetchall()
            for pokemons in results:
                print(pokemons[0])


print_all_pokemon()
