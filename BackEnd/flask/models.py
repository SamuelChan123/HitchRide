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
    password = db.Column('password', db.String(64))
    phone = db.Column('phone', db.String(32))
    rating = db.Column('rating', db.Float())

#-------------------------------------------------------------------------------
class Entry(db.Model):
    __tablename = 'entry'

    id = db.Column('id', db.Integer(), primary_key=True)
    personId = db.Column('personid', db.Integer(), unique=True)
    origin = db.Column('origin',db.Float())
    destination = db.Column('destination', db.Float())
    startTime = db.Column('starttime', db.TIMESTAMP())
    endTime = db.Column('endtime', db.TIMESTAMP())
    radiusMiles = db.Column('radiusmiles', db.Float())
    type = db.Column('type', db.String(32))
    comment = db.Column('comment', db.String(64))


#-------------------------------------------------------------------------------
class Groups(db.Model):
    __tablename__ = 'groups'

    id = db.Column('id', db.Integer(), unique = True, primary_key=True)
    group_members = db.Column('group_members', db.String(128))

#-------------------------------------------------------------------------------
