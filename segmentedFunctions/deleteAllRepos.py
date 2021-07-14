import subprocess
import json
import os
import re
import shutil
import calcHoursLate


def deleteAllRepos(repoFileNames):
	for repos in repoFileNames:
			subprocess.run(["rm", repos], check=True, stdout=subprocess.PIPE).stdout 
