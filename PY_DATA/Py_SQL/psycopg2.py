import psycopg2 as pg2
secret = 'xyz'
conn = pg2.connect(database='dvdrental',user='postgres',password=secret)
cur = conn.cursor()
cur.execute('SELECT * FROM payment')

data = cur.fetchmany(10)
data = [] # [(17503,341,2,1528,Decimal('7.99'),datetime.datetime(2007,2,15,22,25,46,996577)),(17504,1,1,1,1,1,1)]
data[0][4] # Decimal('7.99')
conn.close()