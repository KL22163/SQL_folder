import sqlite3

db = sqlite3.connect('cars.db')
cursor = db.cursor()
sql = 'SELECT * FROM Car;'
cursor.execute(sql)

db.close()