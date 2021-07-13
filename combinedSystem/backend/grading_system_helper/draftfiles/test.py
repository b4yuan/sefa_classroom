from ServerFiles.Grading_system import grade_fun
import filecmp
import os
import time
import multiprocessing

yourpath = '/Users/alexgieson/Desktop/'

path = f'{yourpath}testAssignmentStudent'
expectedIn = f'{yourpath}testAssignmentProf/inputs'
expectedOut = f'{yourpath}testAssignmentProf/outputs'
makefile = f'{yourpath}testAssignmentProf/makefile'
maxTimeLimit = 5
TIMEOUT = False

def pro1():
	score, feedback = grade_fun(path, expectedIn, expectedOut, makefile)
	q.put(feedback)
	q.put(score)

def pro2(p1,timelimit):
	t1 = time.time()
	t2 = time.time()
	while (t2 - t1 < timelimit):
		t2 = time.time()
	p1.terminate()

q = multiprocessing.Queue()
p1 = multiprocessing.Process(target=pro1)
p2 = multiprocessing.Process(target=pro2, args=(p1,maxTimeLimit))

p1.start()
p2.start()
p1.join()
result = q.qsize()
if (result == 0):
	TIMEOUT = True
elif (result == 2):
	score = q.get()
	feedback = q.get()
else:
	print("There is error inside")
p2.terminate()

if (TIMEOUT == True):
	score = 0
	feedback = ["Exceed the max time limit"]
else:
	for line in feedback:
		print(line)
	print(f'\nyour score is: {score}')

# os.chdir(path)
# comp = filecmp.cmp('temp.txt', '/Users/alexgieson/Desktop/hw14/outputs/output2.txt', shallow=False)
# print(comp)

