from urllib.request import urlopen
import os

probnum = input("what problem are we trying to do today?\n")
minimal = "https://projecteuler.net/minimal=" + str(probnum)
problem = "https://projecteuler.net/problem=" + str(probnum)


content = urlopen(minimal)
html = content.read().decode("utf-8")

title = urlopen(problem).read().decode("utf-8")
start = title.find("<h2>") + len("<h2>")
end = title.find("</h2>")



directory = "Problems/problem" + str(probnum)

# just to make sure its not something im already using
if(not os.path.isdir(directory)):
    os.mkdir(directory)

fname = directory + "/README.md"

with open(fname, 'w') as f:
    f.write("# " + title[start:end] + '\n')
    f.write(html)

