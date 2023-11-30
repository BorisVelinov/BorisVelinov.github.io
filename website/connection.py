import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="history_site"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

results = cursor.fetchall()

print(results)

cursor.close()
conn.close()
