#object relational mapper for Flask <--> SQL
#-------------------------------------------------------------------------------
#import modules
from sqlalchemy import sql, orm
from app import db
#-------------------------------------------------------------------------------
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column('name', db.String(64))
    email = db.Column('email', db.String(64))
    phone = db.Column('phone', db.String(32))
    rating = db.Column('rating', db.Float())

#-------------------------------------------------------------------------------
class Entry(db.Model):
    __tablename = 'entry'

    id = db.Column('id', db.Integer(), primary_key=True)
    personid = db.Column('personid', db.Integer(), unique=True)
    originLatitude = db.Column('originLatitude',db.Float())
    originLongitude = db.Column('originLongitude', db.Float())
    destLatitude = db.Column('destLatitude', db.Float())
    destLongitude = db.Column('destLongitude', db.Float())
    startTime = db.Column('starttime', db.TIMESTAMP())
    radiusMiles = db.Column('radiusmiles', db.Float())
    type = db.Column('type', db.String(32))
    comment = db.Column('comment', db.String(64))


#-------------------------------------------------------------------------------
class Groups(db.Model):
    __tablename__ = 'groups'

    id = db.Column('id', db.Integer(), unique = True, primary_key=True)
    group_members = db.Column('group_members', db.String(128))
    originLatitude = db.Column('originLatitude', db.Float())
    originLongitude = db.Column('originLongitude', db.Float())
    destLatitude = db.Column('destLatitude', db.Float())
    destLongitude = db.Column('destLongitude', db.Float())
    startTime = db.Column('starttime', db.TIMESTAMP())

#-------------------------------------------------------------------------------
