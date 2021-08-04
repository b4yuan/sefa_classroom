# pas_githubclassroom
Scripts to handle Github class room based grading!

## GitHub Classroom
This section will go through everything needed to work with GitHub Classroom

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
A tag points to a specific version of your repository. Creating a tag preserves a specific version of your files, so any changes made after the tag will not be reflected in the tagged version. When we pull the "final_ver" of your repository, it will pull whatever the files looked like at the most recent commit before the tag. More info can be found [here](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/about-releases).

We also collect the date of your submission to calculate how late it has been submitted. The date of the submission will be the date and time of whatever commit the "final_ver" tag refers to. 

You can check the date and time for yourself by typing ```git log -1 --format=%ai [tag name]```.

#### On GitHub.com
To create a tag, you can click on "create a new release" on the right side bar. The only thing that needs to be specified on this page is "Tag Version", which must be "final_ver". Click "Publish Release" and the tag will be created.

If you want to update your submission, delete and re-add the tag. Click on the tags icon next to the branch selector. Click on the name of the tag, and there should be an option to delete the tag in the top right. Deleting the release is the same thing as deleting the tag. 
#### From the Command Line
To create a tag from the command line, type ```git tag [tag name]```. To show all tags that exist for a repository, ```git show```. Once your tag is created, you must ```git push origin [tag name]```. A normal repository push will not include any tag updates.

To update your submission, there are two options. You can either ```git tag [tag name] -f ```, which forces the tag to update, and ```git push origin [tag name] -f```. Or, you can ```git push -d origin [tag name]``` to delete the tag, and then re-add the tag. 

### Viewing the Grade Report
If students want to see their grade and feedback, they can simply navigate to their assignment repository and view gradeReport.txt.
In gradeReport.txt the student can see their overall grade and the feedback for their submission, which lists where they 
may have lost points and why. 

