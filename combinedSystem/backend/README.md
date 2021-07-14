# pas_backend
Backend has all the functionality code for program analysis. There are three main chunk of code in this repository:  
&emsp;1. Database (located in 'databasefiles' folder)  
&emsp;2. Grading system code (located in 'TestCases/GradingInterface' folder)  
&emsp;3. Grading system interface (located in 'TestCases/GradingInterface' folder)  

There is also a folder called 'grading_system_helper' used to store draft files of Grading system code and the Makefile template.

## Table of folders
* [databasefiles](#databasefiles)
* [grading_system_helper](#grading_system_helper)
* [TestCases](#TestCases)

## databasefiles
This folder stores code related to database. We used peewee(sqlite3) to set up our database.  
&emsp;- database.py  
&emsp;&emsp;This file contains the peewee code.  

&emsp;- addToDB.py  
&emsp;&emsp;This file contains some helper functions to manage database.  

## grading_system_helper
This folder does not contain any code that is part of the functionality code. If you are looking for functionality code please move to [TestCases](#TestCases). This folder stores draft code of grading system and the Makefile template.  
&emsp;- grading_system_helper/draftfiles  
&emsp;&emsp;This folder stores draft codes of Grading system code, and it does not contain any code that is part of the functionality code.  

&emsp;- [Makefile](grading_system_helper/Makefile)  
&emsp;&emsp;This is the template for the Makefile that is one of the key elements of the grading system code. Any developer should read   this template before modifying gradingsystem.py. Any professor user should read this template to create the corresponding Makefile of an assignment.

## TestCases
This folder stores code of grading system, code of grading system interface, code of changing grading parameters feature, and a test folder of the grading system.  
&emsp;- TestCases/Sort2Testcases  
&emsp;&emsp;This folder stores all things needed for testing grading system.  

&emsp;- [equation.py](TestCases/GradingInterface/equation.py)  
&emsp;&emsp;This file contains code of changing grading parameters feature.  

&emsp;- [gradingsystem.py](TestCases/GradingInterface/gradingsystem.py)  
&emsp;&emsp;This file contains code of grading system. This is the core file of backend. The grading system will take path to the project as input. The grading system will output pointslist and feedback. The grading system can check: 1. Is the student file compileable? 2. Can the student file output the expected output given the expected input? 3. How many byte does the student file leak? 4. Will the student file get into an infinite loop?  

&emsp;- [interface.py](TestCases/GradingInterface/interface.py)   
&emsp;&emsp;This file contains code of grading system interface. Meaning frontend user can use grading system through calling functions in this file. There is no need to call functions in gradingsystem.py. 

&emsp;- [grade_submission.py](grade_submission.py)   
&emsp;&emsp;This file contains code of grading system interface as well as the means to input arguments to output two text files, one containing the grade and the other the feedback for a specified homework of a user. It serves as a very streamlined way to run the grading system through a single command. Running the file with the -h or -help argument will show the arguments needed for the code to function.
