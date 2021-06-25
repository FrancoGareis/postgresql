import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="t00tmanyw0rds")