-- Creates the MySQL server user user_0d_1.
-- Creates user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . *
TO 'test'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- when we grant some privileges for a user, running the command flush privileges will reloads the grant tables in the mysql database enabling the changes to take effect without reloading or restarting mysql service
FLUSH PRIVILEGES;
