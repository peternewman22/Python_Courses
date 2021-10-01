"""
1. Create database and table in sqlite3
2. Insert rows of data
3. Create database and table in postgresql
4. Fetch rows from sqlite3
5. Insert into postgresql database
"""

import sqlite3
import csv
sqlitedb = "test.db"

create_tutor_table = """
        CREATE TABLE IF NOT EXISTS tutors(
            id integer PRIMARY KEY,
            first_name text NOT NULL,
            surname text NOT NULL,
            phone_number text NOT NULL,
            email text NOT NULL,
            dob date,
            start_date date,
            end_date date
        );
    """

def csv_to_tuple(csv_fn):
    with open(csv_fn, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return tuple(map(lambda each_list: tuple(each_list), reader))

# Creating database
def create_database(db_name):
    db = sqlite3.connect(db_name)
    db.close()

def create_table(db_name, create_table_command):
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    cur.execute(create_table_command)
    cur.close()
    db.close()

def insert_rows(db_name, table_name, data):
    pass
    

def main():
    print("Creating Database")
    create_database(sqlitedb)
    print("Creating the tutor table")
    create_table(sqlitedb, create_tutor_table)
    print("Inserting rows")
    insert_rows


# if __name__=="__main__":
#     main()

csv_to_tuple("tutors.csv")


