# pas_githubclassroom
Scripts to handle Github class room based grading!

## GitHub Classroom
This section will go through everything needed to work with github classroom

### Setting up GitHub Classroom
GitHub has extensive documentation to look at. Start here: 
https://github.blog/2020-03-18-set-up-your-digital-classroom-with-github-classroom/

### Setting up an Assignment
There are 2 ways to go about this using our system: set up a batch of assignments, add a single assignment.
These methods are outlined below.
Additionally, the following video can also be used for reference:
https://www.youtube.com/watch?v=6QzKZ63KLss

#### Batch of Assignments
FILL IN

#### Single Assignment
FILL IN

#### Sending the Assignment Link to Students
FILL IN


## Grading
This section will cover how to grade assignments with the grading system

### Deploying the System
To use the grading system, this repository needs to be cloned to a server (or computer), which can be done using the following terminal command:
```git clone https://github.com/PurdueCAM2Project/pas_githubclassroom```

Then, install all packages needed to run the grading system by running ```pip3 install -r requirements.txt``` in the terminal.

Lastly, install valgrind on ther server or computer you are using. This can be done using ```apt-get install valgrind``` or ```sudo apt-get install valgrind```.

## Student Side
This section will go over how students will access and submit assignments.

### Accessing an Assignment
To access an assignment, the student must click the assignment link given by the professor. From there, the student will
be prompted to clone the repository and have a copy they can edit and submit from.

### Submitting an Assignment
In order to submit an assignment, the student must push their completed code to their assignment repository. Then, they 
must tag their submission as 'final_ver', which tells the grading system it is ready to be graded. Without the 'final_ver' 
tag, the submission will not be graded.
 
### Tagging an Assignment
#### On GitHub.com
To create a tag, you can click on "create a new release" on the right side bar. The only thing that needs to be specified on this page is "Tag Version", which must be "final_ver". Click "Publish Release" and the tag will be created!
#### From the Command Line

### Viewing the Grade Report
If students want to see their grade and feedback, they can simply navigate to their assignment repository and view gradeReport.txt.
In gradeReport.txt the student can see their overall grade and the feedback for their submission, which lists where they 
may have lost points and why. 

