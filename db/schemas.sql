CREATE TABLE raw_messages (id INTEGER  NOT NULL PRIMARY KEY, user INTEGER  NOT NULL, message text, time INTEGER  NOT NULL);
CREATE TABLE places (id integer primary key,
name text, type integer, lat real, lon real, address text);
CREATE TABLE statuses (user INTEGER  NOT NULL PRIMARY KEY, tg_id integer not null, status INTEGER  NOT NULL);
