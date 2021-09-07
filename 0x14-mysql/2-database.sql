--  New database.
-- -------------------------
-- Execution in terminal:
-- cat 2-database.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS tyrell_corp;

USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT DEFAULT 1, name VARCHAR(256));

INSERT INTO nexus6 (name) VALUES ('Leon');

GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
