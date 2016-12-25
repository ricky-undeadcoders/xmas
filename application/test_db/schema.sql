DROP TABLE if EXISTS users;
DROP TABLE if EXISTS dolls;
DROP TABLE if EXISTS doll_instance;

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY ASC,
  user_name text NOT NULL,
  password text NOT NULL,
  first_name text,
  last_name text,
  email text NOT NULL
);
create table dolls (
  doll_id text PRIMARY KEY,
  user_id INTEGER,
  create_date text NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);
create table doll_instance (
  doll_instance_id INTEGER PRIMARY KEY ASC,
  doll_id text,
  user_id INTEGER NOT NULL,
  create_date text NOT NULL,
  comment text,
  latitude text NOT NULL,
  longitude text NOT NULL,
  location_desc text NOT NULL,
  initial_instance boolean NOT NULL,
  FOREIGN KEY(doll_id) REFERENCES dolls(doll_id),
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);