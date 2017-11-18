drop table if EXISTS statuses;
drop table if EXISTS raw_messages;
drop table if EXISTS places;
CREATE TABLE statuses (user INTEGER  NOT NULL PRIMARY KEY, tg_id integer not null, status INTEGER  NOT NULL);
CREATE TABLE raw_messages (id INTEGER  NOT NULL PRIMARY KEY, user INTEGER  NOT NULL, message text, time INTEGER  NOT NULL, first_name text, last_name text, username text);
CREATE TABLE places(
  id INT,
  name TEXT,
  type INT,
  lat REAL,
  lon REAL,
  address TEXT,
  photo TEXT
);
