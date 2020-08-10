#!/usr/bin/python3
""" using sql alchemy to create a new database called states"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column


Base = declarative_base()


class State(Base):
        """State class, creates a mysql table called states"""
        __tablename__ = "states"

        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(128), nullable=False)
