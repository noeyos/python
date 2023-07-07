# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="python",
        host="localhost",
        port=3304,
        database="python"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute(
    "SELECT e_id, e_name, gen, addr FROM EMP")

for e_id, e_name, gen, addr in cur: 
    print(f"e_id: {e_id}, e_name: {e_name}, gen: {gen}, addr: {addr}")
    
conn.close()
