import sqlite3
import csv
import psycopg2
from decouple import config
from datetime import datetime

USER=config("USER")
PASSWORD=config("PASSWORD")

def prep_values_from_csv(csv_fn):
    with open(csv_fn, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skips over the header row
        values = []
        for l in reader:
            values.append((int(l[0]),l[1],l[2],l[3],l[4],datetime.strptime(l[5],"%d/%m/%Y")))
        return tuple(values)
        

def main():
    print("connecting to sqlite db")
    db1 = sqlite3.connect("test.db",detect_types=sqlite3.PARSE_DECLTYPES)
    print("successfully connected to sqlite db")
    cur1 = db1.cursor()
    print("getting rid of the old values in the db")
    cur1.execute("DROP TABLE IF EXISTS tutors")

    print("Creating tutors table (if not exists)")
    cur1.execute("""
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
        """)

    print("Writing values")
    cur1.executemany("INSERT INTO tutors(id, first_name, surname, phone_number, email, dob) VALUES (?, ?, ?, ?, ?, ?)", prep_values_from_csv("tutors.csv"))
  
    print("Grabbing values from test.db and checking that the typing worked")
    
    cur1.execute("SELECT * FROM tutors")
    rows = cur1.fetchall()
    print(rows)
    for row in rows:
        for val in row:
            print(f"{val}: {type(val)}")
    print("Finishing up!")
    cur1.close()
    db1.close()

    # print("Logging into tutors")
    # db2 = psycopg2.connect(f"dbname=Tutoring user={USER} password={PASSWORD} port=5433")
    # cur2 = db2.cursor()
    # print("Successfully logged into the database")
    # cur2.executemany("INSERT INTO tutors (id,first_name,surname,phone_number,email,dob) VALUES (%s, %s, %s, %s, %s, %s)",rows)
    # # print("committing changes")
    # # cur2.commit()

    # cur2.execute("SELECT * FROM tutors")
    # new_data = cur2.fetchall()
    # print(new_data)
    # cur2.close()
    # db2.close()


if __name__=="__main__":
    main()


# for each_value in prep_values_from_csv("tutors.csv"):
#     print(f"{each_value}: {type(each_value)}")