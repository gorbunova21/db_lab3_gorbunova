import csv
import psycopg2

username = 'GorbunovaSofia'
password = '2003'
database = 'lab_2'
host = 'localhost'
port = '5432'

OUTPUT_FILE = 'Gorbunova_03_DB_{}.csv'

TABLES = [
    'books',
    'authors',
    'genres',
    'ratings'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE.format(table_name), 'w', encoding='UTF-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])