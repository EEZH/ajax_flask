import sqlite3


conn = sqlite3.connect("data.db")
cursor = conn.cursor()

query_create_table_users = """
    CREATE TABLE users (
    id INTEGER PRIMARY KEY
    , name VARCHAR(50) NOT NULL
    )
"""

query_create_table_users_data = """
    CREATE TABLE users_data (
    id INTEGER PRIMARY KEY
    ,user_id INTEGER NOT NULL
    ,email VARCHAR(50) not null
    ,age INTEGER NOT NULL
    ,about VARCHAR(300) NOT NULL
    ) 
"""

# cursor.execute(query_create_table_users)
# cursor.execute(query_create_table_users_data)
# conn.commit()

users = [
    ("Harry",),
    ("Tom",),
    ("Bob",),
    ("Sid",),
    ("Polly",),
    ("Monique",),
    ("Harry Oldman",),
    ("Bob Marley",),
    ("Sid Mayers",),
    ("Harry Kane",)
]

users_data = [
    (1, "har@box.com", 19, "Tro-lo-lo"),
    (2, "tommy@box.ru", 25, "hrrrrrrrr"),
    (3, "bo-bo@post.com", 15, "tsssssssss"),
    (4, "sd@post.post", 45, "silent"),
    (5, "pPol@post", 35, "defoult"),
    (6, "lady@box.com", 52, "Tru-lu-lu"),
    (7, "actor@box.ru", 41, "brrrrrrrr"),
    (8, "sing@post.com", 66, "kaaar"),
    (9, "gamer@post.post", 35, "nois"),
    (10, "storm@post", 24, "lamp")
]

query_add_users = """
INSERT INTO users
(name) VALUES (?)
"""

query_add_users_data = """
INSERT INTO users_data
(user_id, email, age, about)
VALUES
(?,?,?,?)"""

cursor.executemany(query_add_users, users).executemany(query_add_users_data, users_data)
conn.commit()
