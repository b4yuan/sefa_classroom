## Introduction
&emsp;The purpose of this developer manual is to help a user know how to use our grading system by calling functions in [Grading System Interface](https://github.com/PurdueCAM2Project/pas_backend/blob/main/TestCases/GradingInterface/interface.py).  
If you are interested in understanding our code in detail and be able to add more functions to our grading system, please read the [developer_manual](developer_manual.md).  
&emsp;In this user manual, we will mainly focuse on introducing [Grading System Interface](https://github.com/PurdueCAM2Project/pas_backend/blob/main/TestCases/GradingInterface/interface.py) and the [Makefile template](https://github.com/PurdueCAM2Project/pas_backend/blob/main/documentation/Makefile).    

## Grading_system_interface

&emsp; The grading system will be tested under four conditions: correct answer, answer with compile error, answer with memory leak, answer with wrong output.
check one example of the testcase: [testcase exmaple](https://github.com/PurdueCAM2Project/pas_backend/blob/main/TestCases/hw18.py).  


## Makefile
&emsp;As a user, you need to set up your own Makefile according to our [Makefile template](https://github.com/PurdueCAM2Project/pas_backend/blob/main/documentation/Makefile) to be able to use our grading system. 
The Makefile will need Name of the excutable, Name of all the input arguments, Name of all the output files, Name of all the expected output files. There will be
more instructions on how to set up the Makefile in [Makefile template](https://github.com/PurdueCAM2Project/pas_backend/blob/main/documentation/Makefile).  


## Makefile_example
&emsp;go to TestCases/2020homeworks, there are Makefiles for each homeworks
