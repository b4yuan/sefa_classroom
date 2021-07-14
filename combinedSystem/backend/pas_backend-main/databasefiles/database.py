from peewee import *

## this file holds the classes that serve as models for the database tables
# run this file to create the database file
# import the classes to add to the database using peewee

db = SqliteDatabase("autog.sqlite3")

# database class that is model for the table holding the user information
class User(Model):
    client_id = CharField()
    Client_secret = CharField()
    Email = CharField()
    Admin = CharField()

    class Meta:
        database = db


# database class that is a model for the table holding all the oauth information
class Oauth(Model):
    client_id = CharField()
    Client_secret = CharField()
    Authorization_code_id = CharField()
    Authorization_code = CharField()
    Access_token = CharField()
    Refresh_token = CharField()
    User_information = CharField()

    class Meta:
        database = db


# database class that is a model for the table holding all the assignment information
class Assignment(Model):
    Assignment_name = CharField()
    Due = DateTimeField()
    End = DateTimeField()
    Start = DateTimeField()
    Visible_date = DateTimeField()
    Expected_output_file = CharField()
    Expected_input_file = CharField()
    Makefile = CharField()

    class Meta:
        database = db


# database class that is a model for the table holding all the submission information
class Submission(Model):
    Client_id = CharField()
    Assignment_name = CharField()
    Assignment_id = CharField()
    Submission_time = DateTimeField()
    Filename = CharField()
    Fileadd = CharField()
    Score = IntegerField()

    class Meta:
        database = db


# code to run to create the database correctly
if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Oauth, Assignment, Submission])