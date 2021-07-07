import subprocess
import json
import os
import re
import shutil
import calcHoursLate


def startGradingProcess(runFilePath):
	subprocess.run(["python3", "pas_backend/run_grader.py"], check=True, stdout=subprocess.PIPE).stdout
	
