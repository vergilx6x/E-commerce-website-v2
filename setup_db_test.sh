-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS web_test_db;
CREATE USER IF NOT EXISTS 'web_test'@'localhost' IDENTIFIED BY 'Testpassword6.';
GRANT ALL PRIVILEGES ON `web_test_db`.* TO 'web_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'web_test'@'localhost';
FLUSH PRIVILEGES;