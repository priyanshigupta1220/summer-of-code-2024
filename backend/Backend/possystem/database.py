from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import psycopg2
import psycopg2.extras
DB_CONNECTION_STRING="postgresql://postgres:backend@localhost:5432/POSSystem"
conn=psycopg2.connect(DB_CONNECTION_STRING)
cursor=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
