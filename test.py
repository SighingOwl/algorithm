import re

def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])

print("")
def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))

print("")

def parse3():
    for line in open("log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))

print("")

def parse4():
    for line in open("log.txt", "rw"):
        print(" ".join(line.split()[3:5].strip("[]")))

print("")

def parse5():
    for line in open("log.txt"):
        print(re.split("\[|\]", line)[1])

parse1()
parse2()
parse3()
#parse4()
parse5()

