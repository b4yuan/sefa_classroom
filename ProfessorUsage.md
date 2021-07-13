# Setup

## Variables to set

1. '''orgName''': Your organization's name
    * Ex: '''https://github.com/Purdue-ECE264''' then '''orgName = "Purdue-ECE264"'''
2. '''authName''': Your github username
3. '''authKey''': GPG key

## Github API Authorization

1. Go to <https://github.com/settings/tokens>
2. Click '''Generate new token'''
3. Add a Note and check the following scopes:
    * [x] repo
    * [x] admin:org
4. Generate Token copy it
5. Paste key... (This step will be finalized when our code is)

## Github Classroom

1. Go to <https://classroom.github.com>
2. Login and click '''New Classroom'''
3. Click '''Create an Organization'''
4. Go through organization setup
    * This organization belongs to:
      * [x] My Personal Account
      * [ ] A business or institution
5. Select the new organization
6. Follow listed steps to add TAs if desired

# Adding Assignments

1. Go to class organization page
    1. Create a new repository
    2. Add Homework files to repository
    3. Change setting of repository:
        * [x] Template Repository

2. Go to your [classroom](https://classroom.github.com/classrooms)
   1. Click '''New Assignment''' **The name must match the json file**
   2. The assignment must be private and the student should **not** have admin access
   3. Please specify the repository created in your organization
   4. Add Autograding tests
      1. Add test, run C, Run Command: '''make test all'''
   5. Share "invitation URL" with students

# Grades

