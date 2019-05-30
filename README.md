# HitchRide: 

By: Samuel Chan, Samarth Kishor, Benny Beinish, Devon Parikh, Reggie Cai, Joshua Kennedy

## Project Purpose

- 43%: Share of Americans who have used ride-hailing apps in the last year
- Even higher for college-age students! 
- Searching facebook groups for rides can be very tedious

#### HitchRide provides a ride-sharing network of students for students

- HitchRide is a straightforward web app that connects college students looking to share rides. 
- HitchRide makes it effortless to enter when you will need a ride, choose your origin and destination, and find other students taking the same trip.
- HitchRide connects you to the other students who need the same ride as you, exchanges your emails ahead of the time so you can meet, and guarantees that they will be a college student, just like you, by requiring a “.edu” email for signup.

## Use Cases
- Students who own a car and will be making either a one-off or recurrent journey can create a carpool group of other students to cover transportation costs
- Students without access to a vehicle can create/search for a group of students to share an Uber/Lyft, substantially reducing per person costs of such services
- Students who are afraid to travel alone and would prefer the company of additional college students 

## Table of Contents

1.  Folder Structure
2.  Dependencies
3.  Database
4.  Running web-app
5.  Injecting Data (GET, POST requests)
6.  Future Improvements
7.  Challenges/Limitations

## 1. Folder Structure

- flask-researchhub: Directory for Flask app
- db-researchhub: setup for PostgreSQL database
- python-scripts: Web-scraping scripts that scrape Duke faculty members from https://scholars.duke.edu

## 2. Dependencies/Requirements

- Package.json lists dependencies needed for React portion of the application.
- Front End
    - React w/ Material UI
- APIs
    - Leaflet
    - Google Maps
    - Uber/Lyft (planned)
    - Axios for HTTP requests
- Server/Database Requirements
    - Flask 1.0.2
    - Python 2.7.16
    - FlaskSQL Alchemy 1.2.18
    - postgres (PostgreSQL) 11.3
- Deployment
    - AWS EC2 Instance (t2 micro, CentOS)
    - Postgres db
    - RDS Database (not connected, although the database exists and is set up)

## 3. Database

- Navigate to Backend/db in the repository. Ensure PostgreSQL is installed on your system
- Run ./setup.sh in a shell. This runs create.sql (creating the schema) and load.sql (loading randomly generated data into the Postgres database).

## 4. Running Web-app

1.  Flask Server (Object-Relational Mapper and RESTful API)
    - Navigate to Backend/flask
    - Run "python app.py"
2.  React App
    - Navigate into FrontEnd
    - Run npm install to download any package.json dependencies. Ensure npm (Node Package Manager) is installed on your machine.
    - Run npm start. In case of error, run "yarn install --> yarn start."
3. For Deployment (AWS)
    - Must change config to external ip address of vm instance, ensure security groups allow ports to be exposed to incoming/outgoing traffic
    - run yarn start 

## 5. Injecting Data (GET, POST requests)

- We used Axios.js package to make HTTP request calls.
- To perform a GET request this syntax was used:

```javascript
// Make a request for a user with a given ID
axios
  .get("server site")
  .then(function(response) {
    // handle success
    console.log(response);
  })
  .catch(function(error) {
    // handle error
    console.log(error);
  })
  .then(function() {
    // always executed
  });
```

- To perform a POST request:

```javascript
axios.post('server site', {
    name 'key',
    name: 'key'
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
```

## 6. Future Improvements

- Use TypeScript and Redux
- Implement/Integrate Uber and Lyft APIs
- Migrate to an Amazon RDS database
- Work on multiple pages/routing (React-router)
- Implement Mobile App (iOS/Android/React Native)
- Login/Verification functionality (backend complete)
- Implement algorithm for pickup on the way (log time search using kd tree)
- Implement ratings feature (backend complete)
- Automatically split the cost and charge the credit cards

## 7. Challenges/Roadblocks

- Git!
- Development locally vs. on the AWS EC2 Instance
- State flow from child to parent components in React
- JS dynamic typing and other quirks
- Data communication between front end and back end
- Learning/Installing the same version of technologies
- Database schema changes affecting both front/back end (ER Model for relational database)

