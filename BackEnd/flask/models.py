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
    rating = db.Column('rating', db.Boolean())

    # leadInfo = orm.relationship('LeadInfo')
    # studentInfo = orm.relationship('StudentInfo')

#-------------------------------------------------------------------------------
class Entry(db.Model):
    __tablename__ = 'entry'

    department = db.Column('department', db.String(64), primary_key=True)

    # leaddept = orm.relationship('LeadDept')
    # scholars = orm.relationship('Scholars')

#-------------------------------------------------------------------------------
class Groups(db.Model):
    __tablename__ = 'groups'

    id = db.Column('id', db.Integer(), db.ForeignKey('person.id'),
                                            primary_key=True)
    website = db.Column('website', db.String(64))
    person = orm.relationship('Person', backref='leadinfo')
    # leaddept = orm.relationship('LeadDept')
    #projectinfo = orm.relationship('ProjectInfo')
    #person = orm.relationship('Person')
    #not sure whether to put above relationship in LeadInfo or in Person

#-------------------------------------------------------------------------------
