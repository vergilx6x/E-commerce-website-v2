##!/usr/bin/python3

import os

# # Setting environment variables
# os.environ['SECRET_KEY'] = 'my_secret_key'
# os.environ['DATABASE_URL'] = 'sqlite:///site.db'
# os.environ['DEBUG'] = 'True'

# Getting environment variables
secret_key = os.getenv('SECRET_KEY')
database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG')

print(f'SECRET_KEY: {secret_key}')
print(f'DATABASE_URL: {database_url}')
print(f'DEBUG: {debug}')