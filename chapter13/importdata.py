import sqlite3
def convert(value):
    if value.startswith("-"):
        return value.strip("-")
    if not value:
        value=None
    return float(value)

conn=sqlite3.connect("food.db")
curs=conn.cursor()

#drop table
curs.execute("DROP TABLE IF EXISTS food")

#crate table
curs.execute('''CREATE TABLE IF NOT EXISTS food(
     id    TEXT    PRIMARY KEY,
     desc  TEXT,
     water FLOAT,
     kcal  FLOAT,
     protein FLOAT,
     fat   FLOAT,
     ash   FLOAT,
     carbs FLOAT,
     fiber FLOAT,
     sugar FLOAT)''')

#insert
insert="INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?)"
for line in open("food.data","r"):
    fields=line.split("&")
    vals=[convert(f) for f in fields]
    curs.execute(insert,vals);

#query    
query="SELECT * FROM food"
for record in curs.execute(query):
    print "record is: "+str(record)
    for value in record:
        print "value is: "+str(value)

#fetchall
curs.execute(query)
print "curs.fetchall() is: "+str(curs.fetchall())

#condition
query="SELECT * FROM food WHERE kcal <= 100 "
print query
curs.execute(query)
#description can output all the row name of table in a list
names=[f[0] for f in curs.description]
print "names is: "+str(names)
names2=curs.description
print "names2 is: "+str(names2)
for row in curs.fetchall():
    for pair in zip(names,row):
        print "%s: %s" % pair

#delete Note:sqlite3 doesn't have a truncate table command
delete='DELETE FROM food WHERE id="12345"'
curs.execute(delete)

conn.commit()
conn.close()