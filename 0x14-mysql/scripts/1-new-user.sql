-- New user for the checker.
-- -------------------------
-- Execution in terminal:
-- cat 1-new-user.sql | mysql -hlocalhost -uroot -p

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost'
IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
