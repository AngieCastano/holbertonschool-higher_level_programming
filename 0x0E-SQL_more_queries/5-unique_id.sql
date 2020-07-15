-- create a table
-- dafault value id to 1. must be unique
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    papeleria VARCHAR(256)
);
