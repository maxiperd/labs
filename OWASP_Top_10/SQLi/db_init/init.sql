CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) VALUES
('admin', 'password123'),
('john_doe', 'johndoepass'),
('jane_smith', 'janesmithpass'),
('alice', 'alicepass'),
('bob', 'bobpass');
