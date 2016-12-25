import os
import sqlite3
from datetime import datetime as DT


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(os.path.join(os.getcwd(), 'mysterious_lee.db'))
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = connect_db()
    with open('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def populate_db_users():
    c = connect_db()

    sample_users = [{'user_name': 'rickyow',
                     'first_name': 'Ricky',
                     'last_name': 'Whitaker',
                     'password': 'abc123',
                     'email': 'this@that.com'},
                    {'user_name': 'Kyle',
                     'password': 'moocow',
                     'email': 'kyle@ML.com',
                     'first_name': 'NULL',
                     'last_name': 'NULL'}]

    insert_stmt = '''
    INSERT INTO users (user_name, password, email, first_name, last_name)
    VALUES (:user_name, :password, :email, :first_name, :last_name)
    '''

    c.executemany(insert_stmt, sample_users)
    c.commit()


def populate_db_dolls():
    c = connect_db()

    sample_dolls = [{'user_id': '1',
                     'doll_id': 'a101',
                     'image_name': '1.jpg',
                     'create_date': DT.now(),
                     'comment': 'la la la comment',
                     'latitude': '30.231781089557472',
                     'longitude': '-97.84698486328125',
                     'location_desc': 'Austin, TX'},
                    {'user_id': '1',
                     'doll_id': 'a102',
                     'image_name': '2.jpg',
                     'create_date': DT.now(),
                     'comment': 'Isnt this the coolest?',
                     'latitude': '30.491284452100203',
                     'longitude': '-97.50091552734375',
                     'location_desc': 'Austin, TX'},
                    {'user_id': '2',
                     'doll_id': 'a103',
                     'image_name': '3.jpg',
                     'create_date': DT.now(),
                     'comment': 'Whhhhooooaaaa differences',
                     'latitude': '30.26916781624759',
                     'longitude': '-97.74699211120605',
                     'location_desc': 'Austin, TX'}]

    insert_stmt = '''
    INSERT INTO dolls(doll_id, user_id, create_date)
    VALUES (:doll_id, :user_id, :create_date)
    '''

    c.executemany(insert_stmt, sample_dolls)
    c.commit()


def populate_db_doll_instance():

    c = connect_db()

    sample_doll_instances = [{'doll_id': 'a101',
                              'user_id': '1',
                              'image_name': '3.jpg',
                              'create_date': DT.now(),
                              'comment': 'This is the first doll instance!',
                              'latitude': '30.265628086637687',
                              'longitude': '-97.72662878036499',
                              'location_desc': 'Austin, TX',
                              'initial_instance': True},
                             {'doll_id': 'a101',
                              'user_id': '1',
                              'image_name': '5.jpg',
                              'create_date': DT.now(),
                              'comment': 'This is the second doll instance!',
                              'latitude': '30.264608769105326',
                              'longitude': '-97.77267694473267',
                              'location_desc': 'Austin, TX',
                              'initial_instance': False},
                             {'doll_id': 'a102',
                              'user_id': '2',
                              'image_name': '6.jpg',
                              'create_date': DT.now(),
                              'comment': 'This is the first doll instance for the second user!',
                              'latitude': '30.21552074817223',
                              'longitude': '-97.70880281925201',
                              'location_desc': 'Austin, TX',
                              'initial_instance': False},
                             {'doll_id': 'a102',
                              'user_id': '2',
                              'image_name': '7.jpg',
                              'create_date': DT.now(),
                              'comment': 'Doll Instance 2, User 2, whhhhaaa!',
                              'latitude': '30.327809588974795',
                              'longitude': '-97.69940435886383',
                              'location_desc': 'Austin, TX',
                              'initial_instance': False}
                             ]

    insert_stmt = '''
    INSERT INTO doll_instance(doll_id, user_id, create_date, comment, latitude, longitude, location_desc, initial_instance)
    VALUES (:doll_id, :user_id, :create_date, :comment, :latitude, :longitude, :location_desc, :initial_instance)
    '''

    c.executemany(insert_stmt, sample_doll_instances)
    c.commit()


if __name__ == "__main__":
    init_db()
    populate_db_users()
    populate_db_dolls()
    populate_db_doll_instance()
