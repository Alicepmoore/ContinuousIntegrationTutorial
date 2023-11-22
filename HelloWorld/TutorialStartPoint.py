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
	RunBatchFile()
	RunGitCommand()

def RunForever():
	WAIT_TIME_SECONDS = 5
	ticker = threading.Event()
	while not ticker.wait(WAIT_TIME_SECONDS):
		PollForChanges()

PollForChanges()
# # RunForever()