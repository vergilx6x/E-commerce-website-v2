##!/usr/bin/python3
import os

class Config:
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG')