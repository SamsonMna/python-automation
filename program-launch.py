import subprocess
subprocess.Popen('usr/bin/gnome-calculator')# starts the program at a given memory location. Object Popen has two methids: poll() and wait()

#Opening a website with python
subprocess.open('website.com') # Also the module webbrowser can also be used with webbrowser.open('website.co')

# Running other python scripts

subprocess.Popen(['~/home/programs/python.py', 'hello.py']) # runs the script hello.py at an given memory location on the system.

# Opening files with default applications

fileObj = open('hello.odt', 'w')
fileObj.write('Hello World!')
fileObj.close()

subproces.Popen(['start', 'hello.odt'], shell=True) # Opens the hello.odt file within the X-windows shell.

 




