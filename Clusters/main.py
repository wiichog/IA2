from tkinter.filedialog import askopenfilename
from utils import NNP

#filename = askopenfilename()
lines = open("1.txt").readlines()
#numberOfClusters = input("Ingrese el numero de clusters ")
NNP(int(3),lines)