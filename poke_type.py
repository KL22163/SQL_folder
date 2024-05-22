#Selecting the SQL database
import sqlite3
DATABASE = "poke_type.db"

#Asking what pokemon types to sort by, search by type
def print_all_pokemon():
    type_1 = int(input("Type 1: "))
    type_2 = int(input("Type 2: "))
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Pokemons.poke_name FROM Pokemons WHERE Pokemons.type_1 = ? AND Pokemons.type_2 = ? OR Pokemons.type_1 = ? AND Pokemons.type_2 = ?;"
        cursor.execute(sql,(type_1, type_2, type_2, type_1))
        results = cursor.fetchall()
        for pokemons in results:
            print(pokemons[0])


if __name__ == "__main__":
    print_all_pokemon()
