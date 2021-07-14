-- Create the database hbtn_0d_usa and the table states on your MySQL server.
-- The database name will be passed as an argument of the mysql command
-- If the table unique_id already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);