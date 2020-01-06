"""
5 steps
1. Connect to DB
2. Cursor (pointer to rows in the DB)
3. SQL query
4. Commit changes to DB
5. Close connection
"""
import psycopg2

connect_str = "dbname = 'MyFirstDB' user='postgres' password='budgieBird22' host ='localhost' port='5432'"


def create_table():
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return(rows)


def delete(item):
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
insert("Apple", 10, 5)
#update(11, 6, "Water Glass")
#delete("Wine Glass")

# print(view())
