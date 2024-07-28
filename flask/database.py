# connecting to database

import mysql.connector as mc

conn = mc.connect(host='localhost' , user = 'root' ,password = 'Abhishek@2002')

# create a cursor to store query and data temporary
cur = conn.cursor()


# create database

create_db_query = """
create database userdata
"""

cur.execute(create_db_query)

# using db userdata

use_query = """
use userdata
"""
cur.execute(use_query)

# create table

create_table_query = """
create table user_record(name varchar(25),
age INTEGER,
address varchar(100),
college varchar(50),
query varchar(500))
"""

# executing query with help of cursor
cur.execute(create_table_query)  



# query to fetch data from db
query_to_fetch = """
select * from user_record
"""

cur.execute(query_to_fetch)
for record in cur.fetchall():
    print(record)


cur.close()
conn.close()