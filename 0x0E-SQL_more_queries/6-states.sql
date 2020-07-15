-- create a table inside a specific databes
-- id primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
     id INT NOT NULL AUTO_INCREMENT,
     name VARCHAR(30) NOT NULL,
     PRIMARY KEY (id)
);
