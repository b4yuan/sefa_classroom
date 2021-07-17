# **Combined Grading System (Github/Brightspace interactions)**
_This article is incomplete. You can help by expanding it._
## _Abstract_
This section describes the system that governs the interactions between the _Github Classroom_ and the server. This includes pulling, running the grading script, tagging, committing, pushing, deleting the repos afterward, and other pertinent functions such as obtaining the information necessary to run these. These functions are all done by Python scripts that make use of OS and Unix commands/functions.

PAS has decided to make use of _Github Classroom_ to facilitate the user grading process (see **Github Classroom** section). This process involves the student supplying their homework submissions to a repository on _Github Classroom_, which is then pulled into the main server. The homework submissions are then processed by this system, graded individually by the actual grading system, and repositories are deleted off of the main server after the changes have applied to the Github and relevant areas of the server. 
## _Detailed Description of System as a Whole_

## _Description of Specific Functionality_

## _Github Classroom_
_Github Classroom_ is a free online service for educators created by Github to provide storage services that can be used for assignment submission. 

## _What are "Tags"?_
Tags are a specific marker used by Github on repositories that serve useful properties relevant to this part of the system. For instance, tags can provide the system with the time of a submission, and can be used to indicate that the repository has been graded. Of course, these tags can be customized to fit the user's purposes. 

One can read more on the specifics of tags on the official github documentation:
https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/managing-tags

or specific notes taken by Leila Yanni: https://github.com/PurdueCAM2Project/pas_githubclassroom/blob/combined/Notes%20on%20Tags.md
## _Github Commands Used and Their Descriptions_
## _Linux Commands Used and Their Descriptions_
## _Current Status of Functionality and What Needs to be Done_
The combined grading system has not been fully implemented. The Github interactions are mostly complete; however, they need to be tested to interact with the actual grading system itself. Interactions with Brightspace are not complete and fully implemented either.

## _Running the System_
As a user, everything is ran from runSystem.py. This is the core script of the system as it integrates all functions into one process. 

### Running runSystem.py
This file should be run from a command line in a Linux based system. It will not work on Windows. There are a few options that can be specified when running. At least one option of the three grade options _must_ be specified for the program to run.

- Grade a single homework: Call the file with the tag `--hw_name` and the name of the homework. The name of the homework can be the full name or even just the number.  
`python3 runSystem.py --hw_name HW02Sort`  
`python3 runSystem.py --hw_name hw02sort`  
`python3 runSystem.py --hw_name 2`  

- Grade a range of homeworks: Call the file with the tag `--hw_range` and two homework names/numbers to specify the start and end of the range. The start and end indexes are inclusive.  
`python3 runSystem.py --hw_range hw02sort hw10cake2`  
`python3 runSystem.py --hw_range 4 15`  
`python3 runSystem.py --hw_range hw03cake 20`

- Grade all homeworks: Call the file with the tag `--grade_all`. This will grade all homeworks for which a professor-created example folder exists in the professor directory.   
`python3 runSystem.py --grade_all`

- Don't delete folders of cloned repositories and grades after running: The `-d` tag will tell the system to _not_ delete the directory of cloned repositories and the directory in which the grades are stored.  
`python3 runSystem.py --hw_range 2 4 -d`  

### What the System Does
The system works in a loop where each homework, if a range is specified, is graded one at a time. For example, all steps are completed for HW2 before moving on to HW3 and so on.
1. The first step of the system is cloning all appropriate repositories. For the specified homework, all student repositories that have the specified submission tag and _don't_ have the graded tag will be cloned. In this step, the submission date of the homework is also collected and the number of hours late that it was submitted is calculated. 
2. Next, the homeworks are graded. Using the GradingInterface, test cases are ran and other tests are performed to calculate a grade for the homework. The grade and feedback are written to a text file that is placed in the grades directory.
3. The grade report text file is copied from the grades directory to the cloned repositories.
4. The grade, without any feedback, is added to a CSV file for easy reference of the professor.
5. Changes are pushed to the student repositories. The first change is the addition of the grade report text file. The second change is the addition of a new tag that specifies that the repository has been graded. 
6. The cloned repositories and the grade folder are deleted from the local computer.

Throughout this process, feedback messages are written to a text file (filteredOutput.txt) for easy reference. 
