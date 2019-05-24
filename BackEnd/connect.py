from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float, DateTime

engine = create_engine("postgresql://postgres:abc123@localhost:5432/hitchride", echo = True)
# Session = sessionmaker(bind=engine)
# session = Session()

meta = MetaData()

person = Table(
   'person', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('email', String), 
   Column('password', String),
   Column('phone', String),
   Column('rating', Float),
)

groups = Table(
   'groups', meta, 
   Column('id', Integer, primary_key = True), 
   Column('group_members', String), 
)

entry = Table(
   'entry', meta, 
   Column('id', Integer, primary_key = True), 
   Column('personid', Integer), 
   Column('origin', Float),
   Column('destination', Float), 
   Column('starttime', DateTime),
   Column('endtime', DateTime),
   Column('radiusmiles', Float),
   Column('type', String),
   Column('comment', String)
)

meta.create_all(engine)

# ins = person.insert()
# ins = person.insert().values(name = 'Ravi', email = 'test@test.com', password = 'test', phone = '555-555-5555', rating = 5.0)
conn = engine.connect()
# result = conn.execute(ins)

# print(conn.execute("\\d+"))

conn.execute(person.insert(), [
   {'name':'test', 'email':'test', 'password':'test', 'phone':'test', 'rating':5.0},
])

conn.close()

# session.commit()
# session.close()








# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# engine = create_engine('sqlite:///college.db', echo = True)
# meta = MetaData()

# students = Table(
#    'students', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('name', String), 
#    Column('lastname', String), 
# )

# ins = students.insert()
# ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
# conn = engine.connect()
# result = conn.execute(ins)

# conn.execute(students.insert(), [
#    {'name':'Rajiv', 'lastname' : 'Khanna'},
#    {'name':'Komal','lastname' : 'Bhandari'},
#    {'name':'Abdul','lastname' : 'Sattar'},
#    {'name':'Priya','lastname' : 'Rajhans'},
# ])

# s = students.select()
# conn = engine.connect()
# result = conn.execute(s)

# for row in result:
#    print (row)

# s = students.select().where(students.c.id>2)
# result = conn.execute(s)

# for row in result:
#    print (row)


# from sqlalchemy.sql import text
# s = text("select students.name, students.lastname from students where students.name between :x and :y")
# conn.execute(s, x = 'A', y = 'L').fetchall()

# stmt = text("SELECT * FROM students WHERE students.name BETWEEN :x AND :y")

# stmt = stmt.bindparams(
#    bindparam("x", type_= String), 
#    bindparam("y", type_= String)
# )

# result = conn.execute(stmt, {"x": "A", "y": "L"})

# The text() function also be produces fragments of SQL within a select() object that 
# accepts text() objects as an arguments. The “geometry” of the statement is provided by 
# select() construct , and the textual content by text() construct. We can build a statement 
# without the need to refer to any pre-established Table metadata. 

# from sqlalchemy.sql import select
# s = select([text("students.name, students.lastname from students")]).where(text("students.name between :x and :y"))
# conn.execute(s, x = 'A', y = 'L').fetchall()

# from sqlalchemy.sql import select
# s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
# result = conn.execute(s)

# for row in result:
#    print (row)