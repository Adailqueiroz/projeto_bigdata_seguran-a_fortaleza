import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="seguranca_fortaleza"
)

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM bairros;")
total = cursor.fetchone()[0]

print("Total de registros encontrados:", total)

cursor.execute("SELECT * FROM bairros LIMIT 5;")
rows = cursor.fetchall()

print("\nPrimeiras linhas:")
for r in rows:
    print(r)

cursor.close()
conn.close()
