#!/bin/bash
set -e

# Start MySQL service
service mysql start

# Wait for MySQL to start
sleep 5

# Set up the database and user
mysql -e "CREATE DATABASE IF NOT EXISTS ${WEB_MYSQL_DB};"
mysql -e "CREATE USER '${WEB_MYSQL_USER}'@'localhost' IDENTIFIED BY '${WEB_MYSQL_PWD}';"
mysql -e "GRANT ALL PRIVILEGES ON ${WEB_MYSQL_DB}.* TO '${WEB_MYSQL_USER}'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"

# Activate the virtual environment and run Flask
source /home/$USERNAME/app/env_bash.sh
source /home/$USERNAME/app/web_env/bin/activate
exec /home/$USERNAME/app/web_env/bin/python3 run.p