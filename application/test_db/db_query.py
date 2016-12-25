from init_db import connect_db

db = connect_db()

users = db.execute('Select * from users').fetchall()
dolls = db.execute('SELECT * FROM dolls').fetchall()
doll_instances = db.execute('SELECT * FROM doll_instance').fetchall()


select_stmt = '''
SELECT di.* FROM dolls d
JOIN doll_instance di
ON d.doll_id = di.doll_id
'''
test = db.execute(select_stmt).fetchall()

# for doll_join in test:
#     print doll_join

#
# print users
print dolls
print doll_instances

doll_ids = db.execute('SELECT doll_id FROM dolls').fetchall()
print doll_ids
for di in doll_ids:
    print di

for di in doll_instances:
    print di
#
# for user in users:
#     print user
#     print user['first_name']