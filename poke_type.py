import sqlite3

DATABASE = "poke_type.db"

def print_all_pokemon():
    type = input("Search by what type/s?: ")
    with sqlite3.connect(DATABASE) as db