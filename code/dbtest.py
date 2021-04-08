import sqlite3

con = sqlite3.connect("dbtesting.db")
cur = con.cursor()

#create table
# cur.execute('''CREATE TABLE RECIPES
#                 ([recipes] text, [ingredients] text)''')

cur.execute('''INSERT INTO RECIPES VALUES('lettuce burger', 'just lettuce') ''')

con.commit()

cur.execute('''SELECT * FROM RECIPES''')
alll = cur.fetchall()
for i in alll:
    print(i)

con.close()