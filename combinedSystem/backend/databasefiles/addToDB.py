from datetime import datetime as dt
from .database import User, Oauth, Assignment, Submission
import uuid
from Grading_system import grade
import os
from zipfile import ZipFile

def addUser(clientID, clientSecret, email, admin):
    """
    :param clientID: client ID
    :type clientID str
    :param clientSecret: client Secret
    :type clientSecret str
    :param email: email
    :type email str
    :param admin: admin? (0 for no, 1 for yes)
    :type admin int
    :return:
    """

    newUser = User.create(client_id=clientID, Client_secret=clientSecret, Email=email, Admin=admin)

    newUser.save()

    return 0

def addOauth(clientID, clientSecret, authCodeID, authCode, accessToken, refreshToken, userInfo):
    """
    :param clientID: client ID
    :type clientID str
    :param clientSecret: client Secret
    :type clientSecret str
    :param authCodeID: auth code ID
    :type authCodeID str
    :param authCode: auth code
    :type authCode str
    :param accessToken: access token
    :type accessToken str
    :param refreshToken: refresh token
    :type refreshToken str
    :param userInfo: user info
    :type userInfo str
    :return:
    """

    newTokens = Oauth.create(client_id=clientID, Client_secret=clientSecret,
                                   Authorization_code_id=authCodeID, Authorization_code=authCode,
                                   Access_token=accessToken, Refresh_token=refreshToken, User_information=userInfo)

    newTokens.save()

    return 0


def addAssignment(name, start, due, end, visible, expectedIn, expectedOut, makefile):
    """
    :param name: name
    :type name str
    :param start: start date
    :type start datetime
    :param due: due date
    :type due datetime
    :param end: end date
    :type end datetime
    :param visible: visible date
    :type visible datetime
    :param expectedIn: path of expected inputs
    :type expectedIn str
    :param expectedOut: path of expected outputs
    :type expectedOut str
    :param makefile: path of makefile
    :type makefile str
    :return:
    """

    newAssignment = Assignment.create(Assignment_Name=name, Due=due, End=end,
                                      Start=start, Visible_date=visible, Expected_output_file=expectedOut,
                                      Expected_input_file=expectedIn, Makefile=makefile)

    newAssignment.save()

    return 0


def addSubmission(id, assignmentName, file):
    """
    :param id: client id
    :type id str
    :param assignmentName: assignment name
    :type assignmentName str
    :param file: path of file
    :type file file
    :return: grade, feedback
    """

    assignmentID = uuid.uuid1()

    path = f'/root/submissions/{id}/{assignmentName}/{assignmentID}'

    data = file.read()

    with open(f'{path}.zip', 'w+') as file:
        file.write(data)
        with ZipFile(f'{path}.zip', 'r') as zip:
            zip.extractall(f'{assignmentID}')

    newSubmission = Submission.create(Assignment_id=assignmentID, Client_id=id, Assignment_Name=assignmentName,
                                      Submission_time=dt.now(), Filename=filename,
                                      Fileadd=path, Score=-1)
    expected_inputs_path = Assignment.get(Assignment.name == assignmentName).expectedIn
    expected_output_path = Assignment.get(Assignment.name == assignmentName).expectedOut
    makefile_path = Assignment.get(Assignment.name == assignmentName).makefile

    grade, feedback = grade(path, expected_inputs_path, expected_output_path, makefile_path)

    newSubmission.Score = grade

    newSubmission.save()

    return grade, feedback



