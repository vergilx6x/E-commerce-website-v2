#!/usr/bin/python3
""" holds class Cart"""

from app.models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Cart(BaseModel, Base):

    __tablename__ = 'carts'
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    
 

    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)