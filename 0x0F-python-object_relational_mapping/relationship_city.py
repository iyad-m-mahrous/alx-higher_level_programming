#!/usr/bin/python3
""" 14. city model """

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id: State id
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
