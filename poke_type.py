#Selecting the SQL database
import sqlite3
DATABASE = "poke_type.db"

#Asking what pokemon types to sort by, search by type
def print_all_pokemon():
    type_1 = input("Type 1: ")
    #type_2 = input("Type 2: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT poke_name FROM Typings WHERE type_name = ?;"
        cursor.execute(sql,(type_1))
        results = cursor.fetchall()
        for pokemons in results:
            print(pokemons)


print_all_pokemon()