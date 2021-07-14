import time
import multiprocessing
import os

# This is the maximum time you want to run
maxTimeLimit = 5


def pro1():
	#In this function you can put whatever you want
	#eg: call grade_fun() function

	#If all codes in this function(pro1) can be done 
	#within maxTimeLimit (seconds), everything is fine

	#If all codes in this function exceed the time limit, you can define by yourself
	while(1):
		pass
	q.put(2)
	q.put(3)

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
print(q.qsize())
p2.terminate()
