from tkinter.filedialog import askopenfilename
from utils import *

filename = askopenfilename()
lines = open(filename).readlines()
operations = utils()
operations.analizer(lines,lambda cleanLine: operations.hamWords.append(cleanLine),lambda cleanLine: operations.spamWords.append(cleanLine),"ham")
operations.partitions()
operations.analizer(operations.training,lambda cleanLine: operations.addDictionary(operations.ham,cleanLine),lambda cleanLine: operations.addDictionary(operations.spam,cleanLine),"ham")
a = ""
while a!="salir":
    a = input("What is your name? ")
    print(operations.getPSpamGivenSentence(a.split(" "))*100)
