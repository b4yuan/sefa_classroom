from functions.rmtree import rmtree

[students, hws] = fetchLists(fetchRepos(organization, authName, authKey)) 

rmtree('clones') 
    #removes all cloned folders
rmtree('grades')
    #removes folder of grades
for student in students:
    #removes graded tag if it exists on remote repository 

    #removes grade.txt if it exists on remote repository
