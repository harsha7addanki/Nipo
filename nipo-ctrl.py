from sys import argv
import os

if __name__ == "__main__":
    os.makedirs(argv[1] + "/templates")
    os.chdir(argv[1])
    open("urls.py", "x").close()
    open("views.py", "x").close()
    open("__init__.py", "x").close()
    f = open("run.py","w")
    f.write("from Nipo.runner import main;main()")