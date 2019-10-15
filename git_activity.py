import os

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



def exec_cmd(cmd):
    os.system(cmd)
