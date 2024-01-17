-- script that creates a table users
Create Table IF NOT EXISTS users(id INT PRIMARY KEY AUTO_INCREMENT, email VARCHAR(256) NOT NULL UNIQUE, name VARCHAR(255));
