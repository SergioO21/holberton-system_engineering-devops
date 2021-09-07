-- New user for the replica.
-- -------------------------
-- Execution in terminal:
-- cat 3-replica-user.sql | mysql -hlocalhost -uroot -p

CREATE USER IF NOT EXISTS 'replica_user'@'%'
IDENTIFIED BY 'root';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
