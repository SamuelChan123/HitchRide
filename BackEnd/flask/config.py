#Change username to ensure PostgreSQL db is working
#TODO: Deploy server, React app, and database to a cloud service such as AWS, GCP
SQLALCHEMY_DATABASE_URI = 'postgresql://samchan:dbpasswd@0.0.0.0/researchhub'
SQLALCHEMY_ECHO = True
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 20
