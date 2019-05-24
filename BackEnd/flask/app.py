from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import models
import forms

# To test RESTful API functions (see below), the first several @app.route
# statements will need to be commented out. Comment out ('/person/<name>')
# to use the GET or DELETE methods for persons below. For now, these methods
# can be used for the HTML templates being rendered from /templates
# These will be replaced with front end React files, which use the JSON date
# sent to/from the DB using the API methods.


app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})
CORS(app)

@app.route('/', methods=['GET'])
def home():
    persons = db.session.query(models.Person).all()
    entries = db.session.query(models.Entry).all()
    groups = db.session.query(models.Groups).all()
    return render_template('all-persons.html', persons = persons, entries = entries, groups = groups)

#RESTFUL API methods

#Inserting a row into the Person table
@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    maxID = db.session.query(func.max(models.Person.id)).scalar() #gets current maximum ID in Person table
    new_person = models.Person(id=maxID+1, name=data['name'], email=data['email'], password=data['password'], phone=data['phone'], rating=data['rating'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message' : 'New user created!'})

#Return all Persons (users)
@app.route('/person', methods=['GET'])
def get_all_persons():
    persons = models.Person.query.all()
    output = []
    for person in persons:
        person_data = {}
        person_data['id'] = person.id
        person_data['name'] = person.name
        person_data['email'] = person.email
        person_data['phone'] = person.phone
        person_data['rating'] = person.rating
        output.append(person_data)
    return jsonify({'persons' : output})

#Inserting a row into the Entry table
@app.route('/entry', methods=['POST'])
def create_entry():
    data = request.get_json()
    maxID = db.session.query(func.max(models.Entry.id)).scalar() #gets current maximum ID in Entry table
    new_entry = models.Entry(id=maxID+1, personId=data['personId'], origin=data['origin'], destination=data['destination'], startTime=data['starttime'], endTime=data['endtime'], radiusMiles=data['radiusmiles'], type=data['type'], comment=data['comment'])
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message' : 'New entry created!'})

#Return all Entries
@app.route('/entry', methods=['GET'])
def get_all_entries():
    entries = models.Entry.query.all()
    output = []
    for entry in entries:
        entry_data = {}
        entry_data['id'] = entry.id
        entry_data['personId'] = entry.personId
        entry_data['origin'] = entry.origin
        entry_data['destination'] = entry.destination
        entry_data['starttime'] = entry.startTime
        entry_data['endtime'] = entry.endTime
        entry_data['radiusmiles'] = entry.radiusMiles
        entry_data['type'] = entry.type
        entry_data['comment'] = entry.comment
        output.append(entry_data)
    return jsonify({'entries' : output})



#Get one row in Person by ID
@app.route('/person/<person_id>', methods=['GET'])
def get_one_person(person_id):
        person = db.session.query(models.Person)\
            .filter(models.Person.id == person_id).first()

        if not person:
            return jsonify({'message' : 'No user found!'})

        person_data = {}
        person_data['id'] = person.id
        person_data['name'] = person.name
        person_data['email'] = person.email
        person_data['phone'] = person.phone
        person_data['rating'] = person.rating

        return jsonify({'person' : person_data})

# Delete a Person: in the future, the "admin" row in Person table will be used to determine whether a user (Person) has access to deletion
# Also must add function to promote a Person to admin
@app.route('/person/<person_id>', methods=['DELETE'])
def delete_person(person_id):
    #add admin permissions
    # if not current_user.admin:
    #     return jsonify({'message' : 'Cannot perform that function!'})
    person = db.session.query(models.Person)\
        .filter(models.Person.id == person_id).first()

    if not person:
        return jsonify({'message': 'No user found!'})

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message' : 'The user has been deleted!'})



#Get one row in Person by ID
@app.route('/entry/<entry_id>', methods=['GET'])
def get_one_entry(entry_id):
        entry = db.session.query(models.Entry)\
            .filter(models.Entry.id == entry_id).first()

        if not entry:
            return jsonify({'message' : 'No entry found!'})

        entry_data = {}

        entry_data['id'] = entry.id
        entry_data['personId'] = entry.personId
        entry_data['origin'] = entry.origin
        entry_data['destination'] = entry.destination
        entry_data['startTime'] = entry.startTime
        entry_data['endTime'] = entry.endTime
        entry_data['type'] = entry.type
        entry_data['radiusMiles'] = entry.radiusMiles
        entry_data['comment'] = entry.comment

        return jsonify({'entry' : entry_data})

# Delete a Person
@app.route('/entry/<entry_id>', methods=['DELETE'])
def delete_entry(entry_id):

    entry = db.session.query(models.Entry)\
        .filter(models.Entry.id == entry_id).first()

    if not entry:
        return jsonify({'message': 'No entry found!'})

    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message' : 'The entry has been deleted!'})


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
