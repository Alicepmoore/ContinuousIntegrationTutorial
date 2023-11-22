import threading
import time
import os
import sys
import subprocess

def RunBatchFile():
	args = ['VS_Build.bat']
	try:
		result = subprocess.run(args, shell=True, capture_output=True, check=True)
		print(result.stdout.decode("ascii"))
	except subprocess.CalledProcessError as e:
		print("VS Build Error: \n", e.stdout.decode("ascii"))

def RunGitCommand():
	args = ['git', 'status']
	try:
		result = subprocess.run(args, capture_output=True, check=True)
		print(result.stdout.decode("ascii"))
	except subprocess.CalledProcessError as e:
		print("Git Command Error: \n", e.stderr.decode("ascii"))
		

def PollForChanges():
    print(time.ctime())
    previous_status = RunGitCommand()
    while True:
        time.sleep(60)  # Check every 60 seconds
        current_status = RunGitCommand()
        if current_status != previous_status:
            print("Changes detected!")
            previous_status = current_status
            RunBatchFile()

def RunForever():
	WAIT_TIME_SECONDS = 60;
	ticker = threading.Event()
	while not ticker.wait(WAIT_TIME_SECONDS):
		PollForChanges()

PollForChanges()
RunForever()