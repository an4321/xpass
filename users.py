from dotenv import load_dotenv
from os import getenv

import libsql_experimental as libsql

load_dotenv()

url = getenv("TURSO_DATABASE_URL")
auth_token = getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("xpass.db", sync_url=url, auth_token=auth_token)
conn.sync()

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username VARCHAR(255) UNIQUE NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL
);
""")

conn.execute("INSERT INTO users(username, email, password) VALUES ('name_1', 'name@mail.com', 'password_1');")
conn.commit()

print(conn.execute("select * from users").fetchall())

