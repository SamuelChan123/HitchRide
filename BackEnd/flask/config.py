#Change username to ensure PostgreSQL db is working
#TODO: Deploy server, React app, and database to a cloud service such as AWS, GCP
SQLALCHEMY_DATABASE_URI = 'postgresql://ec2-user:12341234@0.0.0.0/hitchride'
#RDS: SQLALCHEMY_DATABASE_URI = 'postgresql://hitchride:password@hitchridedb.c6gkhaxmrqno.us-east-1.rds.amazonaws.com/hitchride
SQLALCHEMY_ECHO = True
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 20
