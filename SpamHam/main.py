from tkinter.filedialog import askopenfilename
from utils import *
import pickle

filename = askopenfilename()
lines = open(filename).readlines()
operations = utils()
operations.analizer(lines,lambda cleanLine: operations.hamWords.append(cleanLine),lambda cleanLine: operations.spamWords.append(cleanLine),"ham")
operations.partitions()
operations.analizer(operations.training,lambda cleanLine: operations.addDictionary(operations.ham,cleanLine),lambda cleanLine: operations.addDictionary(operations.spam,cleanLine),"ham")
operations.saveDicts(operations.ham,"ham")
operations.saveDicts(operations.spam,"spam")
operations.saveDicts(operations.crossValidation,"crossValidation")
operations.saveDicts(operations.test,"test")
