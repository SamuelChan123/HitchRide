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

@app.route('/')
def home():
    persons = db.session.query(models.Person).all()
    projects = db.session.query(models.ProjectInfo).all()
    return render_template('all-persons.html', persons = persons, projects = projects)

#RESTFUL API methods

#Inserting a row into the Person table
@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    maxID = db.session.query(func.max(models.Person.id)).scalar() #gets current maximum ID in Person table
    new_person = models.Person(id=maxID+1, name=data['name'], email=data['email'], password=data['person'], phone=data['phone'], admin=False)
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
        output.append(person_data)
    return jsonify({'persons' : output})

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


#Project proposal
#Adds row to ProjectInfo, rows to ProjectSubject (for each subject), row to LeadInfo based on the manager and user email provided
@app.route('/project', methods=['POST'])
def create_project():
    data = request.get_json()
    #gets manager id based on email and password
    #Gets the id of the manager with the same email and password as the email and password sent in via JSON
    validManager = db.session.query(models.Person)\
        .filter(models.Person.email == data['manager_email'], models.Person.password == data['manager_password']).first()
    if not validManager:
        return jsonify({'message' : 'Incorrect email or password'})
    #Autoincrement project ID pid
    maxID = db.session.query(func.max(models.ProjectInfo.pid)).scalar()

    new_proj = models.ProjectInfo(pid=maxID + 1, name=data['projectname'], num_spots=data['num_spots'], date_posted=data['date_posted'], description=data['description'],
    skills_description=data['skills_description'], manager_id=validManager.id)
    db.session.add(new_proj)
    #If there is no manager in LeadInfo with this id, add it (website is optional)
    newLead = db.session.query(models.LeadInfo)\
        .filter(models.LeadInfo.id==validManager.id).first()
    if not newLead:
        if not 'manager_website' in data:
            db.session.add(models.LeadInfo(id=validManager.id))
        else:
            db.session.add(models.LeadInfo(id=validManager.id, website=data['manager_website'])) #add to LeadInfo

    if 'subject1' in data:
        db.session.add(models.ProjectSubject(pid=maxID+1, subject=data['subject1']))
    if 'subject2' in data:
        db.session.add(models.ProjectSubject(pid=maxID+1, subject=data['subject2']))
    if 'subject3' in data:
        db.session.add(models.ProjectSubject(pid=maxID+1, subject=data['subject3']))

    db.session.commit()
    return jsonify({'message' : 'New project posted!'})

#Return all projects and their Lead's info (from Person and LeadInfo tables)
@app.route('/project', methods=['GET'])
def get_all_projects():
    projects = models.ProjectInfo.query.all()
    output = []
    for project in projects:
        subjects = db.session.query(models.ProjectSubject)\
            .filter(models.ProjectSubject.pid == project.pid).all()
        project_data = {}
        project_data['pid'] = str(project.pid)
        project_data['name'] = str(project.name)
        project_data['num_spots'] = str(project.num_spots)
        project_data['date_posted'] = str(project.date_posted)
        project_data['description'] = str(project.description)
        project_data['skills_description'] = str(project.skills_description)
        if len(subjects)==1:
            project_data['subject1'] = str(subjects[0].subject)
            project_data['subject2'] = ""
            project_data['subject3'] = ""
        if len(subjects)==2:
            project_data['subject1'] = str(subjects[0].subject)
            project_data['subject2'] = str(subjects[1].subject)
            project_data['subject3'] = ""
        if len(subjects)>=3:
            project_data['subject1'] = str(subjects[0].subject)
            project_data['subject2'] = str(subjects[1].subject)
            project_data['subject3'] = str(subjects[2].subject)
        if len(subjects)==0:
            project_data['subject1'] = ""
            project_data['subject2'] = ""
            project_data['subject3'] = ""
        project_lead = db.session.query(models.Person)\
            .filter(models.Person.id == project.manager_id).first()
        project_data['manager_name'] = project_lead.name
        project_data['manager_email'] = project_lead.email
        project_data['manager_phone'] = project_lead.phone
        output.append(project_data)
    return jsonify({'projects' : output})

#Return a single project based on id
@app.route('/project/<project_id>', methods=['GET'])
def get_one_project(project_id):
        project = db.session.query(models.ProjectInfo)\
            .filter(models.ProjectInfo.pid == project_id).first()
        subjects = db.session.query(models.ProjectSubject)\
            .filter(models.ProjectSubject.pid == project_id).all()
        if not project:
            return jsonify({'message' : 'No project found!'})

        project_data = {}
        project_data['pid'] = project.pid
        project_data['name'] = project.name
        project_data['num_spots'] = project.num_spots
        project_data['description'] = project.description
        project_data['date_posted'] = project.date_posted
        project_data['skills_description'] = project.skills_description
        if len(subjects)==1:
            project_data['subject1'] = str(subjects[0].subject)
            project_data['subject2'] = ""
            project_data['subject3'] = ""
        if len(subjects)==2:
            project_data['subject1'] = str(subjects[0].subject)
            project_data['subject2'] = str(subjects[1].subject)
            project_data['subject3'] = ""
        if len(subjects)>=3:
            project_data['subject1'] = str(subjects[0].subject)
            project_data['subject2'] = str(subjects[1].subject)
            project_data['subject3'] = str(subjects[2].subject)
        if len(subjects)==0:
            project_data['subject1'] = ""
            project_data['subject2'] = ""
            project_data['subject3'] = ""

        project_lead = db.session.query(models.Person)\
            .filter(models.Person.id == project.manager_id).first()
        project_data['manager_name'] = project_lead.name
        project_data['manager_email'] = project_lead.email
        project_data['manager_phone'] = project_lead.phone
        return jsonify({'project' : project_data})

#Delete a project
@app.route('/project/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = db.session.query(models.ProjectInfo)\
        .filter(models.ProjectInfo.pid == project_id).first()

    if not project:
        return jsonify({'message': 'No project found!'})

    db.session.delete(project)
    db.session.commit()
    return jsonify({'message' : 'The project has been deleted!'})


#get all rows in Scholars table. This is a list of Duke faculty/researchers and their contact information. (Not to be confused with PIs added to Person/LeadInfo)
@app.route('/scholars/', methods=['GET'])
def get_all_scholars():
    scholars = models.Scholars.query.all()
    output = []
    for scholar in scholars:
        scholars_data = {}
        scholars_data['name'] = scholar.name
        scholars_data['title'] = scholar.title
        scholars_data['department'] = scholar.department
        scholars_data['phone'] = scholar.phone
        scholars_data['email'] = scholar.email
        scholars_data['website'] = scholar.website
        output.append(scholars_data)
    return jsonify({'scholars' : output})

@app.route('/scholars/<scholar_name>', methods=['DELETE'])
def delete_scholar(scholar_name):
    scholar = db.session.query(models.Scholars)\
        .filter(models.Scholars.name == scholar_name).first()

    if not scholar:
        return jsonify({'message': 'No faculty member!'})

    db.session.delete(scholar)
    db.session.commit()
    return jsonify({'message' : 'Faculty member has been deleted!'})

@app.route('/scholars', methods=['POST'])
def create_scholar():
    data = request.get_json()
    new_scholar = models.Scholar(name=data['name'], title=data['title'], department=data['department'], phone=['phone'], email=['email'], website=data['website'])
    db.session.add(new_scholar)
    db.session.commit()
    return jsonify({'message' : 'New project posted!'})


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
