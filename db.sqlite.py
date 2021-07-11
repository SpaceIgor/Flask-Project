import sqlite3

connection = sqlite3.connect('blog.sqlite')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS posts(Id integer primary key AUTOINCREMENT, Title text, Description text, Date integer)")

cursor.execute("INSERT INTO posts (Title, Description, Date) VALUES ('Anton','programmer', 12/10/2021)")

connection.commit()

connection.close()
