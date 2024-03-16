import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    userName = Column(String(25), nullable=False)
    email = Column(String(411), nullable=False)
    onlineStatus = Column(Boolean)

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favouritePlanets = Column(String(250))
    favouriteCharacters = Column(String(250))
    favouriteVehicles = Column(String(250))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    averageTemp = Column(Integer)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    # favourites_planets = Column(Integer, ForeignKey('favourites.favouritePlanets'))
    favourites = relationship(Favourites)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    race = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    favourites = relationship(Favourites)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    length = Column(Integer)
    crewSize = Column(Integer)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    favourites = relationship(Favourites)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
