# Use the latest Ubuntu Server image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SECRET_KEY='my_secret_key' \
    DATABASE_URL='sqlite:///site.db' \
    DEBUG='True' \
    WEB_ENV='dev' \
    WEB_MYSQL_USER='web_admin' \
    WEB_MYSQL_PWD='Testpassword6.' \
    WEB_MYSQL_HOST='localhost' \
    WEB_MYSQL_DB='web_db'



# Update the package list, install necessary packages, and clean up cache
RUN apt-get update && apt-get install -y \
    apt-utils \
    mysql-server \
    python3 \
    vim \
    net-tools \
    curl \
    python3-pip \
    python3-venv \
    pkg-config \
    libmysqlclient-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user with a specified name
ARG USERNAME=admin
RUN adduser --disabled-password --gecos "" $USERNAME

# Set the password for the non-root user and root
RUN echo "$USERNAME:vergil" | chpasswd && \
    echo "root:vergil" | chpasswd

# Set up the working directory as root
WORKDIR /home/$USERNAME/app

# Start MySQL service and configure admin user and password
RUN service mysql start && /bin/bash -c "cat /home/admin/app/setup_db.sh | mysql"

# Create the virtual environment as root
RUN python3 -m venv /home/admin/app/web_env

# Change ownership of the app directory to the non-root user
RUN chown -R $USERNAME:$USERNAME /home/$USERNAME/app

# Switch to the non-root user
# USER $USERNAME

# Install Python dependencies in the virtual environment
COPY requirements.txt /home/$USERNAME/app/
RUN web_env/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /home/$USERNAME/app/

# Expose necessary ports
EXPOSE 5000
EXPOSE 80

# ENTRYPOINT ["/bin/bash", "-c", "source /home/admin/app/env_bash.sh && source /home/admin/app/web_env/bin/activate && web_env/bin/python3 run.py"]

# ENTRYPOINT ["/bin/bash", "-c", "source /home/admin/app/env_bash.sh && source web_env/bin/activate && /bin/bash"]
ENTRYPOINT ["/bin/bash", "-c", "source /home/admin/app/env_bash.sh && source /home/admin/app/web_env/bin/activate && service mysql start && cat /home/admin/app/setup_db.sh | mysql && mysql web_db < data_dump.sql && exec /bin/bash"]

# ENTRYPOINT ["/bin/bash", "-c", "source /home/admin/app/env_bash.sh && source /home/admin/app/web_env/bin/activate && service mysql start && cat /home/admin/app/setup_db.sh | mysql && mysql web_db < data_dump.sql && nohup python3 -m run.py > flask_output.log 2>&1"]