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
    admin = db.Column('admin', db.Boolean())

    # leadInfo = orm.relationship('LeadInfo')
    # studentInfo = orm.relationship('StudentInfo')

#-------------------------------------------------------------------------------
class Departments(db.Model):
    __tablename__ = 'departments'

    department = db.Column('department', db.String(64), primary_key=True)

    # leaddept = orm.relationship('LeadDept')
    # scholars = orm.relationship('Scholars')

#-------------------------------------------------------------------------------
class LeadInfo(db.Model):
    __tablename__ = 'leadinfo'

    id = db.Column('id', db.Integer(), db.ForeignKey('person.id'),
                                            primary_key=True)
    website = db.Column('website', db.String(64))
    person = orm.relationship('Person', backref='leadinfo')
    # leaddept = orm.relationship('LeadDept')
    #projectinfo = orm.relationship('ProjectInfo')
    #person = orm.relationship('Person')
    #not sure whether to put above relationship in LeadInfo or in Person

#-------------------------------------------------------------------------------
class LeadDept(db.Model):
    __tablename__='leaddept'

    id = db.Column('id', db.Integer(), db.ForeignKey('leadinfo.id'),
                                            primary_key=True)
    department = db.Column('department', db.String(64),
                                        db.ForeignKey('departments.department'),
                                        primary_key=True)
    leadinfo = orm.relationship('LeadInfo', backref='leaddept')


#-------------------------------------------------------------------------------
#StudentInfo is currently unused in the webapp. In future versions, we plan to
#add a student login and profile.
class StudentInfo(db.Model):
    __tablename__='studentinfo'

    id = db.Column('id', db.Integer(), db.ForeignKey('person.id'),
                                            primary_key=True)
    research_interests = db.Column('research_interests', db.String(128))
    resume = db.Column('resume', db.String(256))
    school = db.Column('school', db.String(30))
    year = db.Column('year', db.Integer())
    person = orm.relationship('Person', backref='studentinfo')

#-------------------------------------------------------------------------------
class ProjectInfo(db.Model):
    __tablename__='projectinfo'

    pid = db.Column('pid', db.Integer(), primary_key=True)
    name = db.Column('name', db.String(64))
    num_spots = db.Column('num_spots', db.Integer())
    date_posted = db.Column('date_posted', db.DateTime())
    description = db.Column('description', db.String(512))
    skills_description = db.Column('skills_description', db.String(256))
    manager_id = db.Column('manager_id', db.Integer(),
                                            db.ForeignKey('person.id'))

    projectsubject = orm.relationship('ProjectSubject')
    person = orm.relationship('Person', backref='projectinfo')




#Used in previous HTML version, unused with React/RESTful API
    @staticmethod
    def edit(old_pid, pid, name, num_spots, date_posted, description,
                                    skills_description, manager_id):
        try:
            db.session.execute('DELETE FROM projectsubject WHERE pid = :pid',
                               dict(pid=old_pid))
            # db.session.execute('DELETE FROM manages WHERE pid = :pid',
            #                    dict(pid=old_pid))
            db.session.execute('UPDATE projectinfo SET pid = :pid, name = :name,num_spots = :num_spots, date_posted = :date_posted, description = :description, skills_description = :skills_description, manager_id =:manager_id'
                               ' WHERE pid = :old_pid',
                               dict(old_pid=old_pid, name=name, num_spots=num_spots, date_posted=date_posted,
                               description=description, skills_description=skills_description, manager_id=manager_id))
            db.session.execute('INSERT INTO projectsubject VALUES(:pid)',
                                dict(pid=pid))
            #db.session.execute(do something for manager_id???)
            # db.session.execute('INSERT INTO manages VALUES(:pid)',
            #                     dict(pid=pid))
        except Exception as e:
            db.session.rollback()
            raise e



#-------------------------------------------------------------------------------
class ProjectSubject(db.Model):
    __tablename__='projectsubject'

    pid = db.Column('pid', db.Numeric(8,0), db.ForeignKey('projectinfo.pid'),
                                                    primary_key=True)
    subject = db.Column('subject', db.String(64), primary_key=True)


#-------------------------------------------------------------------------------
class Scholars(db.Model):
    __tablename__='scholars'

    name = db.Column('name', db.String(128), primary_key=True)
    title = db.Column('title', db.String(256), primary_key=True)
    department = db.Column('department', db.String(256))
    phone = db.Column('phone', db.String(32))
    email = db.Column('email', db.String(128))
    website = db.Column('website', db.String(256))
