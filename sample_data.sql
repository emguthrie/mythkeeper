/* to load the data, just run:
cat sample_data.sql | sqlite3 db.sqlite */

DELETE FROM user;

INSERT INTO user (username, password, gold) VALUES ('admin', 'password', 555);
INSERT INTO user (username, password, gold) VALUES ('user1', 'password', 555);
INSERT INTO user (username, password, gold) VALUES ('user2', 'password', 555);


