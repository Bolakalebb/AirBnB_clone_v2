#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import column, string, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    _tablename_ = 'cities'
    if storage_type == 'db':
	name = Column(String(128), nullable=False)
	state_id = Column(Sting(60), ForeignKey('states.id'), nullable=False)
	places = relationship('Place', backref='cities',
			      cascade='all, delete, delete-orphan')
    else:
    	name = ''
    	state_id = ''
