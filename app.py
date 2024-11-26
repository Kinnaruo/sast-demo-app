import subprocess
import shlex

def run_command(cmd):
	safe_cmd=shlex.split(cmd)
	subprocess.call(safe_cmd)
def greet(name):
	print(f'Hello,{name}!')
def run_command(cmd):
	subprocess.call(cmd,shell=True)

if __name__ == "__main__":
	name=input("Enter your name: ")
	greet(name)

	cmd=input("Enter a command to run: ")
	run_command(cmd)
