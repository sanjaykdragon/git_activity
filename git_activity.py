import os
import time

flip = False

while True:
    if flip == False:
            open("temp.txt", "r") #create a temporary file
            exec_cmd("git add temp.txt")
            exec_cmd("git commit -m \" activity \"")
            exec_cmd("git push -u origin master")
            flip = True
    else:
            os.remove("temp.txt")
            exec_cmd("git commit -m \" activity 2 \"")
            exec_cmd("git push -u origin master")
            flip = False
    time.sleep(24 * 60 * 60) #sleep for 1 day



def exec_cmd(cmd):
    os.system(cmd)
