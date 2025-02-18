import subprocess
from github import Github
import os
import time

def tokenize(name, expi):
    fnamel = [name, ".txt"]
    fname = fnamel.join("")
    f = open(fname, "x")
    subprocess.run(["git", "checkout", "main"])
    subprocess.run(["git","add", fname])
    subprocess.run(["git", "commit","-m", fname])
    subprocess.run(["git", "push", "--all"])
    time.sleep(expi)
    os.remove(fname)
    subprocess.run(["git", "checkout", "main"])
    subprocess.run(["git","add", fname])
    subprocess.run(["git", "commit","-m", fname])
    subprocess.run(["git", "push", "--all"])
    
def exists(token):
    global sr, contents
    g = Github("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")
    repo = g.get_repo("anigamer101/Arkens")
    contents = repo.get_contents("")
    sar = [token, ".txt"]
    var =  sar.join("")
    for content in contents :
        if content.name in var:
            sr = 1
            return("true")
    if not sr == 1 :
        return("false")
def expire(token):
    os.remove(token)
    subprocess.run(["git", "checkout", "main"])
    subprocess.run(["git","add", token])
    subprocess.run(["git", "commit","-m", token])
    subprocess.run(["git", "push", "--all"])